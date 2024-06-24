import os
from flask import Flask, render_template, url_for, redirect, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookhub.db'
db = SQLAlchemy(app)
app.app_context().push()

api = Api(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<Users %r>" % self.id

class Book_cover(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cover = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return "<Book_cover %r>" % self.id

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Genre %r>" % self.id

class Book_chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book_cover.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return "<Book_chapter %r>" % self.id

class Book_page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('book_chapter.id'), nullable=False)
    page = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<Book_page %r>" % self.id

class Book_like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_book = db.Column(db.Integer, db.ForeignKey('book_cover.id'), nullable=False)

    def __repr__(self):
        return "<Book_like %r>" % self.id

class UsersResource(Resource):
    def post(self):
        new_user_data = request.form
        existing_user = Users.query.filter((Users.login == new_user_data['login']) | (Users.email == new_user_data['email'])).first()
        if existing_user:
            return "Пользователь с данной почтой или именем уже существует"
        
        hashed_password = pbkdf2_sha256.hash(new_user_data['password'])

        new_user = Users(login=new_user_data['login'], password=hashed_password, email=new_user_data['email'])
        db.session.add(new_user)
        db.session.commit()

class LoginResource(Resource):
    def post(self):
        login_data = request.form
        if not login_data:
            return "Заполните все поля"

        user = Users.query.filter_by(login=login_data['login']).first()
        if user and pbkdf2_sha256.verify(login_data['password'], user.password):
            session['user_id'] = user.id
            return "Успех"
        else:
            return "Неправильно введены данные"

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book_cover.id'), nullable=False)


api.add_resource(LoginResource, '/api/login')
api.add_resource(UsersResource, '/api/users')

@app.route('/')
@app.route('/home')
def index():
    books = Book_cover.query.all()
    return render_template("index.html", books=books)

@app.route('/book/<int:book_id>')
def book(book_id):
    session['isLike'] = True
    book = Book_cover.query.get_or_404(book_id)
    auth = Users.query.get_or_404(book.author)
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        if Book_like.query.filter_by(id_user=user_id, id_book=book_id).first():
            session['isLike'] = True
        else:
            session['isLike'] = False
    return render_template("book.html", book=book, auth = auth)

@app.route('/favorite/add/<int:book_id>', methods=['POST'])
def add_to_favorites(book_id):
    if 'user_id' not in session:
        return jsonify({'message': 'Пользователь не авторизован'}), 401

    user_id = session['user_id']

    existing_like = Book_like.query.filter_by(id_user=user_id, id_book=book_id).first()

    if existing_like:
        db.session.delete(existing_like)
        session['isLike'] = False
    else:
        favorite = Book_like(id_user=user_id, id_book=book_id)
        session['isLike'] = True
        db.session.add(favorite)

    db.session.commit()

    return redirect(url_for('book', book_id=book_id))



@app.route('/catalog', methods=['GET'])
def catalog():
    search_query = request.args.get('search')
    genre_id = request.args.get('genre')
    author_name = request.args.get('author')
    genres = Genre.query.all()
    books = Book_cover.query

    if genre_id:
        books = books.filter_by(genre_id=genre_id)
    if author_name:
        author = Users.query.filter(Users.login.ilike(f"%{author_name}%")).first()
        if author:
            books = books.filter_by(author=author.id)

    if search_query:
        books = books.filter(Book_cover.title.ilike(f"%{search_query}%"))

    books = books.all()

    return render_template("catalog.html", books=books, genres=genres)




@app.route('/account')
def account():
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        user = Users.query.get(user_id)
        if user:
            favorite_books = Book_cover.query.join(Book_like, Book_like.id_book == Book_cover.id).filter(Book_like.id_user == user_id).all()
            return render_template("account.html", user=user, favorite_books=favorite_books)
        else:
            return "Пользователь не найден"
    else:
        return redirect(url_for('index'))


@app.route('/auth', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        response = LoginResource().post()
        if response != "Успех":
            message = response
        else:
            message = "Авторизация успешна. Можете войти."
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('auth.html', message=message)

@app.route('/registration', methods=['POST', 'GET'])
def register():
    message = None
    if request.method == 'POST':
        response = UsersResource().post()
        if isinstance(response, str):
            message = response
        else:
             message = "Регистрация успешна. Можете войти."
             return redirect(url_for('index'))
    return render_template("registration.html", message=message)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session['user_id'] = 0
    return redirect(url_for('index'))


if __name__ == "__main__":
    #subprocess.Popen(["python", "bot.py"])
    app.run(debug=True)
    
