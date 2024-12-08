from flask import Blueprint, redirect, session

bp = Blueprint("logout", __name__)


@bp.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")
