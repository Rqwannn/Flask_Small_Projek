from flask_login import UserMixin
from datetime import datetime
from app import db # Dari variabel db di file __init__.py

'''
Secara khusus, workouts pada program tersebut merupakan field yang menunjukkan adanya relasi one-to-many antara User dan Workout,
dimana satu User dapat memiliki banyak Workout. Parameter backref='author' menandakan bahwa relasi tersebut akan dapat 
diakses melalui atribut author pada model Workout. lazy=True menandakan bahwa SQLAlchemy akan memuat objek relasi hanya jika 
dibutuhkan (lazy loading).
'''

'''
UserMixin adalah kelas mixin pada Flask-Login yang menyediakan beberapa metode bantu yang dibutuhkan oleh model pengguna. 
Dengan menggunakan UserMixin, kita dapat dengan mudah menambahkan metode-metode yang dibutuhkan oleh Flask-Login ke dalam 
model pengguna kita, seperti is_authenticated, is_active, is_anonymous, dan get_id.
'''

# IF want use many to many under here, Pivot table

# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    workouts = db.relationship('Workout', backref='author', lazy=True) # tambahain uselist=False jika ingin one to one
    # tags = db.relationship('Tag', secondary=tags, backref='users')


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)