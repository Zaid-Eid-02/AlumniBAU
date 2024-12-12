from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, DateField, SubmitField


class EmploymentForm(FlaskForm):
    form_title = "Employment"

    route = "/employment"

    does_work = SelectField(
        "Are you currently working?",
        choices=[(0, "Select"), (1, "Yes"), (2, "No")],
        coerce=int,
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