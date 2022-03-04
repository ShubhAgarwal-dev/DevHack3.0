from flask import Flask, render_templatepip

app = Flask(__name__)


@app.route('/')
def log_in():
    pass


@app.route('/home')
def home():
    pass
