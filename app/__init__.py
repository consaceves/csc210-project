import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "oEHYBreJ2QSefBdUhD19PkxC"
    appdir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        f"sqlite:///{os.path.join(appdir, 'ebay2.db')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    with app.app_context():
        from . import models
        db.drop_all()
        db.create_all()

    from . import models

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(id)

    # blueprint for auth routes in our app
    from . import api
    app.register_blueprint(api.auth.app)

    return app
