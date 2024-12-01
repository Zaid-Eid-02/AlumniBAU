#!/usr/bin/env python
from app import create_app

app = create_app()


if __name__ == "__main__":
    if app.config["DEBUG"]:
        print(app.config)
        print(app.url_map)
        print(app.url_map._rules)
        print(app.url_map._rules_by_endpoint)
    app.run(port=app.config["PORT"], debug=app.config["DEBUG"])
