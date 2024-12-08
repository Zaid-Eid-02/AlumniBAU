from flask import Blueprint, render_template, session
from werkzeug.datastructures import MultiDict
from utils import login_required
from database.repo import repo
from forms.survey.personal import PersonalForm
from forms.survey.academic import AcademicForm
from forms.survey.employment import EmploymentForm
from forms.survey.feedback import FeedbackForm

bp = Blueprint("survey", __name__)


@bp.route("/survey")
@login_required
def survey():
    alumnus = repo.get_alumnus(session.get("username"))
    forms = [
        form(data=alumnus)
        for form in [PersonalForm, AcademicForm, EmploymentForm, FeedbackForm]
    ]
    return render_template("alumni/survey.jinja", forms=forms)
