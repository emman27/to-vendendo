#!/usr/bin/env python
from tovendendo import app, db


if __name__ == "__main__":
    db.create_all(app=app)
    app.run()
