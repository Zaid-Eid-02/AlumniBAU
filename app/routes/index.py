from flask import Blueprint, redirect, session
from app.database.repo import repo
from app.utils import login_required

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    return redirect("/stats" if repo.is_admin(session.get("username")) else "/survey")
