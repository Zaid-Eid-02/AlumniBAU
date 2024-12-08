from flask import Blueprint, redirect, render_template, session
from utils import login_required

bp = Blueprint("news", __name__)


@bp.route("/news")
@login_required
def news():
    return (
        redirect("/announce")
        if session.get("role") == "admin" and "announce" in session.get("perms")
        else render_template("alumni/news.jinja")
    )
