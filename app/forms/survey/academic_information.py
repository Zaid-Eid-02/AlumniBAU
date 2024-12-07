from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length


class AcademicInformationForm(FlaskForm):
    full_name = StringField()
