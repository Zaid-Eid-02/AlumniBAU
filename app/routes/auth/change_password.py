from flask import Blueprint, request, render_template, session, flash, redirect
from app import repo

bp = Blueprint("change_password", __name__)


@bp.route("/change_password", methods=["GET", "POST"])
def change_password():
    """Change user password"""
    if request.method == "GET":
        return render_template("auth/change_password.jinja")

    password = request.form.get("password")
    verification = request.form.get("confirmation")

    if not password:
        return render_template(
            "error.jinja", message="must provide new password", code=400
        )

    if password != verification:
        return render_template("error.jinja", message="passwords don't match", code=400)

    repo.update_password(session["user_id"], password)
    flash("Password Changed Successfully!")
    return redirect("/")
