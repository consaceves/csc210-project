from flask import Blueprint, render_template

app = Blueprint("home_page", __name__)

@app.route("/")
def home():
    return render_template("home.html")