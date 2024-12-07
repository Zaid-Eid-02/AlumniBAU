from flask import Blueprint, redirect, render_template, session
from app.utils import login_required

bp = Blueprint("news", __name__)


@bp.route("/news")
@login_required
def news():
    return (
        redirect("/announce")
        if session["role"] == "admin" and session["announcer"]
        else render_template("alumni/news.jinja")
    )
