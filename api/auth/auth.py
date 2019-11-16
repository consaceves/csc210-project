from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from ... import models, db
from .form import LoginForm, CreateAccountForm
from random import randint

app = Blueprint("home_page", __name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/createaccount", methods=["GET", "POST"])
def createaccount():
    form = CreateAccountForm()
    if form.validate_on_submit():
        print("VALIDATED")
        id = randint(1, 100)
        username = form.username.data
        password = form.password.data
        print(username, password)

        new_user = models.User(id=id, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home_page.login"))
    return render_template("createaccount.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home_page.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        print(user)
        print(form.username.data)
        if user is None or not user.verify_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("home_page.login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("home_page.home"))
    return render_template("login.html", form=form)


@app.route("/hidden")
def hidden():
    return render_template("hidden.html")
