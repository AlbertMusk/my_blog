#encoding:utf-8

from exts import db
from datetime import datetime
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    summary = db.Column(db.String(100),nullable=False)
    aside = db.Column(db.String(100),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    context = db.Column(db.Text,nullable=False)



class SuperUser(db.Model):
    __tablename__ = 'super_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)