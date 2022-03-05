from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        user_name = request.form.get("uname")
        password = request.form.get("pword")
        return redirect(url_for('jk'))
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('extra.html')


@app.route('/home')
def home():
    return render_template('homepage.html')


@app.route('/jk')
def jk():
    name = str(request.args['uname']) or 'default'
    pas = str(request.args['pword']) or 'default'
    return f"It is now working {name} {pas}"


if __name__ == '__main__':
    app.run(debug=True)
