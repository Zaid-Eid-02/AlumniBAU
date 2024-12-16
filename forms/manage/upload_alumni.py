from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class UploadAlumniForm(FlaskForm):
    form_title = "Upload Alumni"
    file = FileField(
        validators=[FileRequired(message="Please select a file to upload")],
        render_kw={"accept": ".csv"},
    )
    submit = SubmitField("Upload")
