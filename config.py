
import os
# python相关配置
DEBUG = True
TEMPLATE_AUTO_UPDATE = True
SECRET_KEY = 'Albert_Musk_Blog'

# 数据库相关配置

DIALECT = 'mysql'
DRIVER = 'pymysql'
HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'blog_demo'
USERNAME = 'root'
PASSWORD = 'root'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False