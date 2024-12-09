from flask import Blueprint, redirect, session
from utils import login_required

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    return redirect("/survey" if session.get("role") == "alumnus"
                    else "/stats" if "stats" in session.get("perms")
                    else "/manage" if "manage" in session.get("perms")
                    else "/announce" if "announce" in session.get("perms")
                    else "/mod" if "mod" in session.get("perms")
                    else "/news")
