from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta

db = SQLAlchemy()

class User(db.Model):
    """Data model for a user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    user_password = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)

    post = db.relationship('Post')

    def __repr__(self):
        """Show info about user."""

        return f"<User_id= {self.user_id} user_name= {self.user_name}>"

class Post(db.Model):
    """Data model for posts to photo board."""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    post_name = db.Column(db.String(), nullable=False)
    post_comment = db.Column(db.String(), nullable=True)
    post_photo_link = db.Column(db.String(), nullable=False)

    user = db.relationship('User')

    def __repr__(self):
        return f"<Post id= {self.post_id}>"

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pics'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)        

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()
    print('Connected to db!')
