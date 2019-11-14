from flask import Blueprint, render_template
from .form import LoginForm

app = Blueprint("home_page", __name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
