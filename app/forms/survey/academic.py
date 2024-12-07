from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, TextAreaField


class AcademicForm(FlaskForm):
    major = StringField(
        render_kw={"disabled": True},
    )

    gpa = FloatField(
        render_kw={"disabled": True},
    )

    graduation_year = IntegerField(
        render_kw={"disabled": True},
    )

    postgraduate = BooleanField()

    reason = TextAreaField()