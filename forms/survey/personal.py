from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, IntegerField, SubmitField


class PersonalForm(FlaskForm):
    form_title = "Personal"
    route = "/personal"
    full_name = StringField(render_kw={"disabled": True})
    phone_number = IntegerField()
    email = EmailField()
    home_address = StringField()
    marital_status = SelectField(
        choices=[
            ("0", "Select"),
            (1, "Single"),
            (2, "Married"),
            (3, "Divorced"),
            (4, "Widowed"),
        ],
        coerce=int,
    )
    save = SubmitField()
