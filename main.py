from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def log_in():
    return render_template('index.html')


@app.route('/home')
def home():
    pass


if __name__ == '__main__':
    app.run()
