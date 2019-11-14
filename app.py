import os
from flask import Flask
from api import auth

if __name__ == "__main__":
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "oEHYBreJ2QSefBdUhD19PkxC"
    app.register_blueprint(auth.app)
    app.run()