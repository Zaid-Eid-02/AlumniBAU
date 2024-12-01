from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from app.routes import index
from app.routes.auth import login, logout, change_password
from app.routes.alumni import survey, news, posts
from app.routes.admin import stats, manage, mod, announce


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.config.from_pyfile("config.py")

    for blueprint in [
        index,
        survey,
        news,
        posts,
        stats,
        manage,
        mod,
        announce,
        login,
        logout,
        change_password,
    ]:
        app.register_blueprint(blueprint.bp)

    @app.after_request
    def after_request(response):
        """Ensure responses aren't cached"""
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    @app.errorhandler(404)
    def not_found(e):
        return render_template("error.jinja", message=str(e)[3:], code=404)

    return app
