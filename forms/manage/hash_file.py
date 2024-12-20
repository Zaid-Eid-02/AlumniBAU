from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class hashFileForm(FlaskForm):
    file_path = StringField("Enter full file path:", validators=[InputRequired()])
    submit = SubmitField("Submit")