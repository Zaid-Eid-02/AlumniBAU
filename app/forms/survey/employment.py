from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField, StringField, DateField


class EmploymentForm(FlaskForm):
    work = BooleanField()

    reason = TextAreaField()

    address = StringField()

    date = DateField()

    title = StringField()
