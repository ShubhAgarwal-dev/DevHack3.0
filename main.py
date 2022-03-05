from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        user_name = request.form.get("uname")
        password = request.form.get("pword")
        return user_name + password
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('extra.html')


@app.route('/home')
def home():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
