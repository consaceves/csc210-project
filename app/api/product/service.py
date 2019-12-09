import uuid
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from flask_mail import Message
from ... import models, db, mail, photos
from .form import UploadProductForm

app = Blueprint("product", __name__)


@app.route("/product/new", methods=["GET", "POST"])
def upload_new_product():
    form = UploadProductForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        description = form.description.data
        condition = form.condition.data

        new_product = models.Product(id=uuid.uuid4(),
                                     name=name,
                                     price=price,
                                     description=description,
                                     condition=condition)
        db.session.add(new_product)
        db.session.commit()
    return render_template("upload.html", form=form)


@app.route("/product/<int:uuid>", methods=["GET"])
def get_product(uuid):
    product = models.Product.query.filter_by(id=uuid).first()
    return product
