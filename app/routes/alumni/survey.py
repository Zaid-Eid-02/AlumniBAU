from flask import Blueprint, render_template
from app.utils import login_required

bp = Blueprint("survey", __name__)


@bp.route("/survey")
@login_required
def survey():
    return render_template("alumni/survey.jinja")
