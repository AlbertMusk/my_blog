#encoding:utf-8

from flask_script import Manager
from my_blog import app
from models import SuperUser,Article,article_tag,Tag
from exts import db
from flask_migrate import Migrate,MigrateCommand


manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
def add_user(username,password):
    user = SuperUser(username=username,password=password)
    db.session.add(user)
    db.session.commit()
    print('超级用户添加完毕')

@manager.option('-t','--tagname',dest='tagname')
def add_tagname(tagname):
    tag = Tag(tag_name=tagname)
    db.session.add(tag)
    db.session.commit()
    print('新建%s标签成功' % tagname)

@manager.command
def init():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
