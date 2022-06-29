from flask import render_template
from gamebase import app, db, mongo
from gamebase.models import Game, Genre, User


@app.route("/")
def home():
    return render_template("base.html")