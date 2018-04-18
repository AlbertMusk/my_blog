# encoding: utf-8
# author = 'Albert_Musk'

from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class SuperUser(db.Model):
    __tablename__ = 'super_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(255),nullable=False)
    create_time = db.Column(db.String(100),default=datetime.now)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result