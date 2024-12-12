from flask import Blueprint, render_template, redirect, session
from utils import login_required

bp = Blueprint("profile", __name__)


@bp.route("/profile")
@login_required
def profile():
    return (
        redirect("/admin/stats/alumnus.jinja")
        if session.get("role") == "admin" and "mod" in session.get("perms")
        else render_template("alumni/profile.jinja")
    )
