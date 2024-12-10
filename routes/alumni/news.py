from flask import Blueprint, redirect, render_template, session

bp = Blueprint("news", __name__)


@bp.route("/news")
def news():
    return (
        redirect("/announce")
        if session.get("role") == "admin" and "announce" in session.get("perms")
        else render_template("alumni/news.jinja")
    )
