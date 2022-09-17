# @Time: 2022/9/17 1:27
# @Author: 李树斌
# @File : 3_1_1hello.py
# @Software :PyCharm
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
boostrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('3-5user.html', name = name)


if __name__ == '__main__':
    app.run()
