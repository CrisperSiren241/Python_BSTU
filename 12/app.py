from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boxes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Box(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    color = db.Column(db.String(20))
    capacity = db.Column(db.Float)

    def __repr__(self):
        return f'<Коробка {self.name}>'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    box_id = db.Column(db.Integer, db.ForeignKey('box.id'), nullable=False)
    box = db.relationship('Box', backref=db.backref('items', lazy=True))

    def __repr__(self):
        return f'<Предмет {self.name}>'

color_codes = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'magenta': '#800080'
}

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    count = Box.query.count()
    return render_template('index.html', count=count)

@app.route('/boxes', methods=['GET', 'POST'])
def boxes():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        capacity = round(float(request.form['capacity']), 1) 

        if color not in color_codes:
            error_message = 'Неверный цвет. Допустимые цвета: ' + ', '.join(color_codes.keys())
            return render_template('error.html', error_message=error_message, boxes=Box.query.all(), color_codes=color_codes)

        if Box.query.filter_by(name=name).first():
            error_message = f'Коробка с именем "{name}" уже создана'
            return render_template('error.html', error_message=error_message, boxes=Box.query.all(), color_codes=color_codes)

        box = Box(name=name, color=color, capacity=capacity)
        db.session.add(box)
        db.session.commit()

        return render_template('success.html', message='Новая коробка создана', boxes=Box.query.all(), color_codes=color_codes)

    boxes = Box.query.all()
    return render_template('boxes.html', boxes=boxes, color_codes=color_codes)

@app.route('/boxes/<box_name>', methods=['GET', 'POST'])
def box_page(box_name):
    box = Box.query.filter_by(name=box_name).first()
    if not box:
        return 'Коробка не найдена', 404

    if request.method == 'POST':
        name = request.form['name']
        volume = float(request.form['volume'])

        total_volume = sum(item.volume for item in box.items)
        if volume > box.capacity - total_volume:
            return render_template('error.html', error_message='Недостаточно места в коробке', box=box, items=box.items, color_codes=color_codes)

        item = Item(name=name, volume=volume, box_id=box.id)
        db.session.add(item)
        db.session.commit()

        return redirect(url_for('box_page', box_name=box_name))

    items = Item.query.filter_by(box_id=box.id).all()
    available_capacity = box.capacity - sum(item.volume for item in items)
    return render_template('box.html', box=box, items=items, color_codes=color_codes, available_capacity=available_capacity)

@app.route('/boxes/<box_name>', methods=['POST'])
def add_item_to_box(box_name):
    name = request.form.get('name')
    volume = float(request.form.get('volume'))

    box = Box.query.filter_by(name=box_name).first()
    if not box:
        return 'Коробка не найдена', 404

    total_volume = sum(item.volume for item in box.items)
    if total_volume + volume > box.capacity:
        return 'Добавление этого предмета приведет к переполнению коробки', 400

    item = Item(name=name, volume=volume, box_id=box.id)
    db.session.add(item)
    db.session.commit()

    return redirect(url_for('box_page', box_name=box_name))

@app.route('/boxes/delete/<box_name>', methods=['POST'])
def delete_box(box_name):
    box = Box.query.filter_by(name=box_name).first()
    if box:
        db.session.delete(box)
        db.session.commit()
    return redirect(url_for('boxes'))

@app.route('/boxes/<box_name>/delete_item/<item_id>', methods=['POST'])
def delete_item(box_name, item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('box_page', box_name=box_name))

if __name__ == '__main__':
    app.run(debug=True)
