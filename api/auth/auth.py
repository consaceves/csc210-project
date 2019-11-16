from flask import Blueprint, render_template
from .form import LoginForm, CreateAccountForm

app = Blueprint("home_page", __name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/createaccount")
def createaccount():
    form = CreateAccountForm()
    return render_template("createaccount.html", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/hidden")
def hidden():
    return render_template("hidden.html")
