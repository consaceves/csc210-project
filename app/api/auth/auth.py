import uuid
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from ... import models, db
from .form import LoginForm, CreateAccountForm

app = Blueprint("home_page", __name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/createaccount", methods=["GET", "POST"])
def createaccount():
    form = CreateAccountForm()
    if form.validate_on_submit():
        id = uuid.uuid4()
        username = form.username.data
        name = form.name.data
        password = form.password.data

        new_user = models.User(id=id,
                               username=username,
                               name=name,
                               password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return render_template("hidden.html", user=current_user.name)
    return render_template("createaccount.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return render_template("hidden.html", user=current_user.username)
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("home_page.login"))
        login_user(user, remember=form.remember_me.data)
        return render_template("hidden.html", user=current_user.name)
    return render_template("login.html", form=form)


@app.route("/hidden")
def hidden():
    if current_user.is_authenticated:
        return render_template("hidden.html", user=current_user.name)
    else:
        return redirect(url_for("home_page.login")), 401


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home_page.login"))


@app.route("/product")
def product():
    return render_template("product.html")