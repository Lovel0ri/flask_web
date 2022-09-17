# @Time: 2022/9/17 2:25
# @Author: 李树斌
# @File : 3_2hello.py
# @Software :PyCharm
from flask_bootstrap import Bootstrap
from flask import Flask,render_template
app = Flask(__name__)
boostrap = Bootstrap(app)

@app.run('/user/<name>')
def hello(name):
    return render_template('3-5user.html')


if __name__ == '__main__':
    app.run()
