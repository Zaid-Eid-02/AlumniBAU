from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, TextAreaField


class FeedbackForm(FlaskForm):
    form_title = "Feedback"

    communicate = BooleanField(
        description="Do you communicate with the university?",
    )

    follow = BooleanField(
        description="Do you follow university activities and events?",
    )

    club = BooleanField(
        description="Do you support creating an alumni club?",
    )

    suggestion = TextAreaField("Do you have any suggestions?")

    save = SubmitField()
