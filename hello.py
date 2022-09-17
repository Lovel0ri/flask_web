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

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('submit')#表单提交按钮
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
