import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import auth

app = Flask(__name__)
app.config["SECRET_KEY"] = "oEHYBreJ2QSefBdUhD19PkxC"

app.config["SECRET_KEY"] = "oEHYBreJ2QSefBdUhD19PkxC"
appdir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"sqlite:///{os.path.join(appdir, 'ebay2.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Blueprints
app.register_blueprint(auth.app)

if __name__ == "__main__":
    # app = Flask(__name__)
    app.run()
