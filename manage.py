from flask_script import Manager
from my_blog import app
from models import SuperUser,Article
from exts import db


manager = Manager(app)

@manager.command
def init():
    db.drop_all()
    db.create_all()
    print('数据库初始化完毕')

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
def add_user(username,password):
    user = SuperUser(username=username,password=password)
    db.session.add(user)
    db.session.commit()
    print('超级用户添加完毕')


if __name__ == '__main__':
    manager.run()
