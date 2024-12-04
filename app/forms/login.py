from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=50)],
        render_kw={"placeholder": "Enter your username", "autofocus": "true"},
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "Enter your password", "id": "password"},
    )
    show_password = BooleanField(
        "Show Password",
        description="<span>Show Password</span>",
        render_kw={
            "onclick": "if(password.type=='text')password.type='password';else password.type='text';",
            "id": "eye",
        },
    )
    submit = SubmitField("Login", render_kw={"class": "submit"})
