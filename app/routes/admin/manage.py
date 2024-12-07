from flask import Blueprint, render_template
from app.utils import manager_required
from app.forms.manage.upload_alumni import UploadAlumniForm
from app.forms.manage.file_path import filePathForm
from app.database.repo import repo

bp = Blueprint("manage", __name__)


@bp.route("/manage")
@manager_required
def manage():
    return render_template("admin/manage/manage.jinja")


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
    return render_template("admin/manage/upload.jinja", form=form, message=message)


@bp.route("/hash", methods=["GET", "POST"])
def hash():
    form = filePathForm()
    message = ""
    if form.validate_on_submit():
        file_path = form.file_path.data
        repo.hash_file(file_path)
        message = f"Successfully hashed {file_path}"
    return render_template("admin/manage/hash.jinja", form=form, message=message)