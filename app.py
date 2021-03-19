from flask import Flask
from flask import request, redirect
# from flask import redirect
from flask import render_template
from flask import session
import os

accountInfo = {"test": "test"}

app = Flask(
    __name__,
    static_url_path="/"
)

app.config['SECRET_KEY'] = os.urandom(24)


@app.route("/", methods=['GET', 'POST'])
def cindex():
    # session.clear()
    return render_template("homePage.html")


@app.route("/signout", methods=['GET', 'POST'])
def index():
    session.clear()
    return redirect('/')


@app.route("/signin", methods=["POST"])
def check():
    Account = request.form["account"]
    PassWord = request.form["password"]
    session['username'] = Account
    if accountInfo.__contains__(Account):
        if(PassWord == accountInfo[Account]):
            print("Success")
            return redirect('/member')
        print("Wrong Password  "+PassWord)
        return redirect("/error")
    print("Wrong Account  "+Account)
    return redirect("/error")


@app.route("/error", methods=["GET", "POST"])
def error():
    return render_template("errorPage.html")


@app.route("/member", methods=['GET', 'POST'])
def userpage():
    username = session.get('username')
    if username:
        return render_template("userPage.html")
    else:
        return redirect('/')


app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run(port=3000)

# app.run(port=3000)
