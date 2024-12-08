from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField, StringField, DateField, SubmitField


class EmploymentForm(FlaskForm):
    form_title = "Employment"

    route = "/employment"

    work = BooleanField(
        description="Are you currently working?",
    )

    reason = TextAreaField(
        label="What reasons prevented you from working?",
    )

    address = StringField(
        "Company Address",
    )

    date = DateField(
        "Date of Employment",
    )

    title = StringField(
        "Job Title",
    )

    save = SubmitField()