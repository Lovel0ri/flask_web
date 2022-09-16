# @Time: 2022/9/16 23:00
# @Author: 李树斌
# @File : hello1.py
# @Software :PyCharm
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {} </p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello,{name}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
