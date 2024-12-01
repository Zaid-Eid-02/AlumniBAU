from flask import Blueprint, render_template, redirect, session
from app.utils import login_required

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    return redirect("/survey" if session.get("user_id") != 1 else "/stats")
