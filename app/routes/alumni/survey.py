from flask import Blueprint, render_template, session
from werkzeug.datastructures import MultiDict
from app.utils import login_required
from app.database.repo import repo
from app.forms.survey.personal_information import PersonalInformationForm
from app.forms.survey.academic_information import AcademicInformationForm

bp = Blueprint("survey", __name__)


@bp.route("/survey")
@login_required
def survey():
    alumnus = MultiDict(dict(repo.get_alumnus(session["username"])))
    print(alumnus)
    forms = [
        form(obj=alumnus) for form in [PersonalInformationForm, AcademicInformationForm]
    ]
    print(forms)
    return render_template("alumni/survey.jinja", forms=forms)
