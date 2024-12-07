from flask import Blueprint, render_template, session
from werkzeug.datastructures import MultiDict
from app.utils import login_required
from app.database.repo import repo
from app.forms.survey.personal import PersonalForm
from app.forms.survey.academic import AcademicForm
from app.forms.survey.employment import EmploymentForm
from app.forms.survey.feedback import FeedbackForm

bp = Blueprint("survey", __name__)


@bp.route("/survey")
@login_required
def survey():
    alumnus = MultiDict(dict(repo.get_alumnus(session.get("username"))))
    forms = [
        form(obj=alumnus)
        for form in [PersonalForm, AcademicForm, EmploymentForm, FeedbackForm]
    ]
    print(forms)
    return render_template("alumni/survey.jinja", forms=forms)
