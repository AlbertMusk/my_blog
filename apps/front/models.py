# encoding: utf-8
# author = 'Albert_Musk'


from exts import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    summary = db.Column(db.String(100),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    context = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return '<%s>' % self.title




article_tag = db.Table(
    'article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)

)

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tag_name = db.Column(db.String(50),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)

    articles = db.relationship('Article', backref='tags', secondary=article_tag)

    def __repr__(self):
        return '<%s>' % self.tag_name
