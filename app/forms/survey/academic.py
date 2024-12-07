from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    IntegerField,
    BooleanField,
    TextAreaField,
    SubmitField,
)


class AcademicForm(FlaskForm):
    form_title = "Academic Information"

    major = StringField(
        render_kw={"disabled": True},
    )

    gpa = FloatField(
        "GPA",
        render_kw={"disabled": True},
    )

    graduation_year = IntegerField(
        render_kw={"disabled": True},
    )

    postgraduate = BooleanField(
        description="Did you complete your postgraduate studies?",
    )

    reason = TextAreaField(
        "What reasons prevented you from completing your postgraduate studies?",
    )

    save = SubmitField()
