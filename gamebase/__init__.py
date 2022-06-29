import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE"] = os.environ.get("DATABASE_URL")



db = SQLAlchemy(app)
mongo = PyMongo(app)

from gamebase import routes # noqa