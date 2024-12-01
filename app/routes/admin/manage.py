from flask import Blueprint, render_template, send_file
from app.utils import manager_required
from app.forms.upload_alumni import UploadAlumniForm
from app.repo import repo

bp = Blueprint("manage", __name__)


@bp.route("/manage")
@manager_required
def manage():
    return render_template("admin/manage.jinja")


@bp.route("/upload", methods=["GET", "POST"])
@manager_required
def upload():
    form = UploadAlumniForm()
    message = ""
    if form.validate_on_submit():
        file = form.file.data
        file_content = file.read().decode("utf-8")
        count = repo.add_alumni(file_content)
        message = f"Successfully added {count} alumni"
    return render_template("admin/upload.jinja", form=form, message=message)
