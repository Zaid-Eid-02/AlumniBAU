from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, TelField, SubmitField


class PersonalForm(FlaskForm):
    form_title = "Personal Information"

    full_name = StringField(
        render_kw={"disabled": True},
    )

    phone_number = TelField()

    email = EmailField()

    address = StringField()

    marital_status = SelectField(
        choices=[(1, "Single"), (2, "Married"), (3, "Divorced"), (4, "Widowed")],
    )

    save = SubmitField()