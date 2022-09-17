# @Time: 2022/9/17 10:48
# @Author: 李树斌
# @File : 3-6hello.py
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
    return render_template('3-9user.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('3-8_404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('3-8_500.html'),500




if __name__ == '__main__':
    app.run()
