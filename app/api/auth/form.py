from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),
                                                Length(1, 64)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Log In")


class CreateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),
                                                   Length(1, 64)])
    name = StringField("Name", validators=[DataRequired(), Length(1, 64)])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 24)])
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(),
                                                                    Length(8, 24)])
    submit = SubmitField("Create")
