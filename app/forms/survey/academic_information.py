from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length


class AcademicInformationForm(FlaskForm):
    major = StringField(
        render_kw={"disabled": True},
    )
