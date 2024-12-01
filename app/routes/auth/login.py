from flask import Blueprint, render_template, redirect, request, session, flash
from app.forms.login import LoginForm
from werkzeug.security import check_password_hash
from app.repo import repo

bp = Blueprint("login", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    form = LoginForm()

    if request.method == "GET":
        return render_template("auth/login.jinja", form=form)

    if not form.validate_on_submit():
        flash("Invalid credentials.", "danger")
        return render_template("auth/login.jinja", form=form)

    username = form.username.data
    password = form.password.data
    rows = repo.get_users(username)

    if len(rows) and check_password_hash(rows[0]["password_hash"], password):
        session["user_id"] = rows[0]["id"]
        session["user_name"] = rows[0]["username"]
        flash("Logged in as " + session["user_name"], "success")
        return redirect("/")

    flash("Invalid credentials.", "danger")
    return render_template("auth/login.jinja", form=form)
