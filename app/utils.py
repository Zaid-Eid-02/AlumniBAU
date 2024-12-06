from functools import wraps
from flask import redirect, session
from app.database.repo import repo


def login_required(f):
    """
    Decorate routes to require login.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def manager_required(f):
    """
    Decorate routes to require a manager account.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_manager(session.get("username")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    """
    Decorate routes to require an admin account.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_admin(session.get("username")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def data_access_required(f):
    """
    Decorate routes to require access to info.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.has_data_access(session.get("username")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def announcer_required(f):
    """
    Decorate routes to require access to announcements.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_announcer(session.get("username")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def mod_permission_required(f):
    """
    Decorate routes to require mod permissions.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not repo.is_mod(session.get("username")):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function
