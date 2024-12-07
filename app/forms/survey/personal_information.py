from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import InputRequired, Length

class PersonalInformationForm(FlaskForm):
    full_name = StringField(
        render_kw={"disabled": True},
    )
