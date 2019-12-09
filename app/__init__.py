import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos', IMAGES)


def create_app():
    app = Flask(__name__)

    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config["SECRET_KEY"] = "oEHYBreJ2QSefBdUhD19PkxC"
    appdir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        f"sqlite:///{os.path.join(appdir, 'ebay2.db')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'

    db.init_app(app)
    mail.init_app(app)
    configure_uploads(app, photos)

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
    app.register_blueprint(api.product.app)

    return app
