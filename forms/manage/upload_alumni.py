from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired


class UploadAlumniForm(FlaskForm):
    form_title = "Upload Alumni"
    file = FileField(
        validators=[InputRequired(message="Please select a file to upload")]
    )
    submit = SubmitField("Upload")
