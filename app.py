import os
from flask import Flask
from api import auth

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(auth.app)
    app.run()