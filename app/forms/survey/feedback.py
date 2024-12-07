from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField


class FeedbackForm(FlaskForm):

    communicate = BooleanField()

    follow = BooleanField()

    club = BooleanField()

    suggestion = StringField()
