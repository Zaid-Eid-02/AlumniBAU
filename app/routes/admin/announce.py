from flask import Blueprint, render_template
from app.utils import login_required

bp = Blueprint("announce", __name__)


@bp.route("/announce")
@login_required
def announce():
    return render_template("admin/announce.jinja")
