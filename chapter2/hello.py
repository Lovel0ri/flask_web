from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chapter3/index.html')

@app.route('/user/<name>')
def user():
    return render_template('chapter3/user.html', name = name)


if __name__ == '__main__':
    app.run()
