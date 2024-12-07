from flask import Blueprint, redirect, session
from app.database.repo import repo
from app.utils import login_required

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    return redirect("/survey" if session.get("role") == "alumnus"
                    else "/stats" if session.get("alumni_data_access")
                    else "/manage" if session.get("manager")
                    else "/announce" if session.get("announcer")
                    else "/mod") # if session.get("mod_permissions")   
