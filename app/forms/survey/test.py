from wtforms import Form, StringField

class TestForm(Form):
    full_name = StringField()