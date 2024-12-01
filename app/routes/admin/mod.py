from flask import Blueprint, render_template
from app.utils import login_required

bp = Blueprint("mod", __name__)


@bp.route("/mod")
@login_required
def mod():
    return render_template("admin/mod.jinja")
