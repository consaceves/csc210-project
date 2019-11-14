from flask_wtf import FlaskForm
from flask_login import LoginManager
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),
                                             Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Log In")


class CreateAccountForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),
                                             Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 24)])
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(),
                                                                    Length(8, 24)])
    submit = SubmitField("Create")
