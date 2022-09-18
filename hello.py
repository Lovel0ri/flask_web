# @Time: 2022/9/17 10:48
# @Author: 李树斌
# @File : hello.py
# @Software :PyCharm
from flask import Flask, render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_moment import Moment
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath((os.path.dirname(__file__)))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)#db对象是SQLAlchemy类的实例
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('submit')#表单提交按钮

"""定义Role 和 Users模型"""
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)#primary_key设为主键
    name = db.Column(db.String(64),unique = True)#unique不允许出现重复的值
    users = db.relationship('User',backref='role')#建立关系
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer,primary_key = True)#primary_key设为主键
    username = db.Column(db.String(64),unique = True,index = True)#unique不允许出现重复的值，index为列设置索引，提升查询效率
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))#添加外键，建立关系，'roles.id'表明这列的值是roles表中相应行的id值值
    def __repr__(self):
        return '<User %r>' % self.name
"""角色到用户是一对多的关系，一个角色可以属于多个用户，但每个用户都只能有一个角色"""
@app.route('/',methods = ['GET','POST'])
def index():
    # name = None#如果没有值输入就为None
    form = NameForm()#实例化form
    if form.validate_on_submit():#如果能被验证函数接受返回True
        old_name=session.get('name')
        #name = form.name.data把局部变量name保存在用户会话中
        if old_name is not None and old_name != form.name.data:
            flash('看起来你修改了名字')
        session['name'] = form.name.data
        return redirect(url_for('index'))
        # form.name.data=''#把data属性设为空字符串，清空表单字段
    return render_template('index.html',form=form,name=session.get('name'))



@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
