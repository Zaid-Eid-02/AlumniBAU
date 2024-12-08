from flask import Blueprint, render_template, redirect, request, session, flash
from forms.auth.login import LoginForm
from werkzeug.security import check_password_hash
from database.repo import repo

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

    role = form.role.data
    username = form.username.data
    password = form.password.data
    rows = (repo.get_admins if role == "Admin" else repo.get_alumni)(username)
    if len(rows) and check_password_hash(rows[0]["password_hash"], password):
        session["id"] = rows[0]["id"]
        session["username"] = username
        session["role"] = "alumnus"
        if role == "Admin":
            session["role"] = "admin"
            session["perms"] = repo.get_perms(username)
        flash("Logged in as " + username, "success")
        return redirect("/")

    flash("Invalid credentials.", "danger")
    return render_template("auth/login.jinja", form=form)
