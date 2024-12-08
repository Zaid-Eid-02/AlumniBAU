#!/usr/bin/env python
from __init__ import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=app.config["PORT"], debug=app.config["DEBUG"])
