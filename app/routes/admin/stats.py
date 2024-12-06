from flask import Blueprint, render_template
from app.utils import data_access_required
from app.database.repo import repo

bp = Blueprint("stats", __name__)


@bp.route("/stats")
@data_access_required
def stats():
    stats = repo.get_stats()
    return render_template("admin/stats/stats.jinja", stats=stats)


@bp.route("/alumni")
@data_access_required
def alumni():
    alumni = repo.get_all_alumni()
    return render_template("admin/stats/alumni.jinja", alumni=alumni)