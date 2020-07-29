from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(200))
    image_dir = db.Column(db.String(200))
        
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    blog_description = db.Column(db.String(700))
    image_dir_blog = db.Column(db.String(200))
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    #time = db.Column(db.DateTime(timezone=True))

