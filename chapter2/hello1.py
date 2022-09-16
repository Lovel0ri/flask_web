# @Time: 2022/9/16 23:00
# @Author: 李树斌
# @File : hello1.py
# @Software :PyCharm
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/usr/<name>')
def user(name):
    return f'<h1>Hello,{name}!</h1>'.format(name)
