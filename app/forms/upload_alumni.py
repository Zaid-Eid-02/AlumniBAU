from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired


class UploadAlumniForm(FlaskForm):
    file = FileField(
        description="Pick a file:", validators=[InputRequired(message="Please select a file to upload")]
    )
    submit = SubmitField("Upload")
