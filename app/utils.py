from functools import wraps
from flask import redirect, session
from app.repo import repo


def login_required(f):
    """
    Decorate routes to require login.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def manager_required(f):
    """
    Decorate routes to require a manager account.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if repo.is_manager(session.get("user_id")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    """
    Decorate routes to require an admin account.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_admin(session.get("user_id")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def data_access_required(f):
    """
    Decorate routes to require access to info.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_data_access(session.get("user_id")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def announce_access_required(f):
    """
    Decorate routes to require access to announcements.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_announce_access(session.get("user_id")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def mod_permission_required(f):
    """
    Decorate routes to require mod permissions.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_mod_permission(session.get("user_id")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function
