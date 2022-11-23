from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    username = StringField(
        label="Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="Password",
        validators=[InputRequired(), EqualTo("confirm", message="Passwords must match")],
    )
    confirm = PasswordField(label="Confirm Password", validators=[InputRequired()])

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
