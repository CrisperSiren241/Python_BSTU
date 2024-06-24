import os
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app.app_context().push()

api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120), index=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    url = db.Column(db.String(255), index=True)
    release_date = db.Column(db.Integer, index=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    posts = db.relationship('Post', backref='movie', lazy='dynamic')

    def __repr__(self):
        return '<Movie {}>'.format(self.title)
    
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Genre %r>" % self.id

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@app.route('/')
@app.route('/home')
def index():
    works = Movie.query.all()
    return render_template("index.html", works=works)

@app.route('/registration')
def register():
    return render_template("reg.html")

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['login']
    email = request.form['email']
    password = request.form['password']

    new_user = User(username=username, email=email, password=pbkdf2_sha256.hash(password))
    db.session.add(new_user)
    db.session.commit()

    return render_template("index.html")

@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.form['login']
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'exists': True})
    else:
        return jsonify({'exists': False})

@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form['email']
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return jsonify({'exists': True})
    else:
        return jsonify({'exists': False})

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and pbkdf2_sha256.verify(password, user.password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            return render_template("auth.html", error="Invalid credentials")
    return render_template("auth.html")

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login_user'))

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for('login'))
    
    return render_template("profile.html", user=user)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    posts = Post.query.filter_by(movie_id=movie_id).all()
    return render_template('movie.html', movie=movie, posts=posts)

@app.route('/movie/<int:movie_id>/submit_opinion', methods=['POST'])
def submit_opinion(movie_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login_user'))
    
    content = request.form['content']
    new_post = Post(content=content, user_id=user_id, movie_id=movie_id)
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(url_for('movie_detail', movie_id=movie_id))

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id = session.get('user_id')

    if post.user_id != user_id:
        flash('You do not have permission to delete this post.', 'danger')
        return redirect(url_for('movie_detail', movie_id=post.movie_id))

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('movie_detail', movie_id=post.movie_id))

if __name__ == "__main__":
    app.run(debug=True)
    
