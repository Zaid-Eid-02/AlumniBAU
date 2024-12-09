from flask import Blueprint, render_template, session
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


@bp.route("/personal", methods=["POST"])
@login_required
def personal():
    alumnus = repo.get_alumnus(session.get("username"))
    form = PersonalForm(data=alumnus)
    if form.validate_on_submit():
        repo.update_personal(session.get("username"), form.data)
    return survey()


@bp.route("/academic", methods=["POST"])
@login_required
def academic():
    alumnus = repo.get_alumnus(session.get("username"))
    form = AcademicForm(data=alumnus)
    if form.validate_on_submit():
        repo.update_academic(session.get("username"), form.data)
    return survey()


@bp.route("/employment", methods=["POST"])
@login_required
def employment():
    alumnus = repo.get_alumnus(session.get("username"))
    form = EmploymentForm(data=alumnus)
    if form.validate_on_submit():
        repo.update_employment(session.get("username"), form.data)
    return survey()


@bp.route("/feedback", methods=["POST"])
@login_required
def feedback():
    alumnus = repo.get_alumnus(session.get("username"))
    form = FeedbackForm(data=alumnus)
    if form.validate_on_submit():
        repo.update_feedback(session.get("username"), form.data)
    return survey()
