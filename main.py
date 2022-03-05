from flask import Flask, render_template, request, redirect, url_for
from pyweb.first import user_db

user_database = user_db(r'database\user.db')

app = Flask(__name__)

user_name = 'ShubhAgarwal'


@app.route('/', methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        global user_name
        user_name = request.form.get("uname")
        # password = request.form.get("pword")
        if user_database.check_user_img2(user_name) > 0:
            return redirect(url_for('home'))
    return render_template('index.html')


@app.route('/home')
def home():
    name = str(request.args['uname']) or 'default'
    return render_template('homepage.html', name=name)


@app.route('/profile')
def profile():
    return render_template('profilepage.html')


@app.route('/jk')
def jk():
    name = str(request.args['uname']) or 'default'
    pas = str(request.args['pword']) or 'default'
    return f"It is now working {name} {pas}"


if __name__ == '__main__':
    app.run(debug=True)
