from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('tem_chapter3/../templates/index.html')

@app.route('/user/<name>')
def user():
    return render_template('tem_chapter3/../templates/user.html', name = name)


if __name__ == '__main__':
    app.run()
