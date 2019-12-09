from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import Length, DataRequired


class UploadProductForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(),
                                                Length(1, 300)])
    price = IntegerField("Price", validators=[DataRequired()])
    description = TextAreaField("Description")
    condition = StringField("Condition", validators=[DataRequired(), Length(1, 15)])
    submit = SubmitField("Upload product")