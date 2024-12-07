from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SelectField


class PersonalForm(FlaskForm):
    national_number = IntegerField(
        render_kw={"disabled": True},
    )

    full_name = StringField(
        render_kw={"disabled": True},
    )

    phone_number = IntegerField()

    email = EmailField()

    address = StringField()

    marital_status = SelectField(
        choices=[("Single"), ("Married"), ("Divorced"), ("Widowed")],
    )
