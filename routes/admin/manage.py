from flask import Blueprint, flash, render_template
from utils import admin_required, manager_required
from forms.manage.upload_alumni import UploadAlumniForm
from forms.manage.hash_file import hashFileForm
from database.repo import repo

bp = Blueprint("manage", __name__)


@bp.route("/manage")
@admin_required
@manager_required
def manage():
    return render_template("admin/manage/manage.jinja")


@bp.route("/upload", methods=["GET", "POST"])
@admin_required
@manager_required
def upload():
    form = UploadAlumniForm()
    if form.validate_on_submit():
        count = repo.add_alumni(form.file.data)
        flash(f"Successfully added {count} alumni")
    return render_template("admin/manage/upload.jinja", form=form)


@bp.route("/hash", methods=["GET", "POST"])
@admin_required
@manager_required
def hash():
    form = hashFileForm()
    if form.validate_on_submit():
        repo.hash_file(form.file_name.data)
        flash(f"Successfully hashed {form.file_name.data}")
    return render_template("admin/manage/hash.jinja", form=form)


@bp.route("/admins")
@admin_required
@manager_required
def admins():
    admins = repo.get_all_admins()
    return render_template("admin/manage/admins.jinja", admins=admins)