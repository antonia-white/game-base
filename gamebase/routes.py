from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from gamebase import app, db, mongo
from gamebase.models import Game, Genre, User


# GAMES - DB
@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if email exists in db
        existing_user = User.query.filter(User.email == \
                                           request.form.get("email").lower()).all()

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                    # TODO: - grab fname from user db to display on login
                        session["user"] = request.form.get("email").lower()
                        flash("Hello")
                        # .format(request.form.get("fname")))
                            # session["user"]))
                        return redirect(url_for(
                            "get_games", email=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login"))

        else:
            # email doesn't exist
            flash("Incorrect Email and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/get_games")
def get_games():
    games = list(Game.query.order_by(Game.title).all())
    consoles = list(mongo.db.consoles.find())
    genres = list(Genre.query.all())
    return render_template("games.html", games=games, genres=genres, consoles=consoles)


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    # genre = list(Genre.query.order_by(genre_name).all())
    # if "user" not in session or session["user"] != "admin":
    #     flash("You must be admin to manage games!")
    #     return redirect(url_for("get_games"))

    # Grab list of all genres from genre database
    genres = list(Genre.query.order_by(Genre.genre_name).all())
    consoles = list(mongo.db.consoles.find())
    if request.method == "POST":
        user = User.query.filter(User.email == \
            session['user']).first()
        # print("user: " + str(user.__dict__))
        # Create an instance of game
        game = Game(
            #"id": request.form.get("id"),
            title=request.form.get("title"),
            developer=request.form.get("developer"),
            release_date=request.form.get("release_date"),
            is_singleplayer=bool(True if request.form.get("is_singleplayer") else False),
            image_url=request.form.get("image_url"),
            genre_id=request.form.get("genre"),
            user_id=user.id,
            console=request.form.get("console")
        )

        db.session.add(game)
        db.session.commit()
        return redirect(url_for("get_games"))
    return render_template("add_game.html", genres=genres, consoles=consoles)


@app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    # if "user" not in session or session["user"] != "admin":
    #     flash("You must be admin to manage games!")
    #     return redirect(url_for("get_games"))
    consoles = list(mongo.db.consoles.find())
    genres = list(Genre.query.order_by(Genre.genre_name).all())
    game = Game.query.get_or_404(game_id)
    user = User.query.filter(User.email == \
            session['user']).first()
    if request.method == "POST":
        game.title=request.form.get("title")
        game.developer=request.form.get("developer")
        game.release_date=request.form.get("release_date")
        game.is_singleplayer=bool(True if request.form.get("is_singleplayer") else False)
        game.image_url=request.form.get("image_url")
        game.genre_id=request.form.get("genre")
        game.console=request.form.get("console")
        game.user_id=user.id
        db.session.commit()
        return redirect(url_for("get_games"))
    return render_template("edit_game.html", game=game, genres=genres, consoles=consoles)


@app.route("/delete_game/<int:game_id>")
def delete_game(game_id):
    # if session["user"] != "admin":
    #     flash("You must be admin to manage games!")
    #     return redirect(url_for("get_games"))

    game = Game.query.get_or_404(game_id)
    db.session.delete(game)
    db.session.commit()
    mongo.db.consoles.delete_many({"game_id": str(game_id)})
    return redirect(url_for("get_games"))

# CONSOLES - MONGO
@app.route("/get_consoles")
def get_consoles():
    consoles = list(mongo.db.consoles.find())
    return render_template("consoles.html", consoles=consoles)


# @app.route("/search", methods=["GET", "POST"])
# def search():
#     query = request.form.get("query")
#     consoles = list(mongo.db.consoles.find({"$text": {"$search": query}}))
#     return render_template("consoles.html", consoles=consoles)


@app.route("/add_console", methods=["GET", "POST"])
def add_console():
    # if "user" not in session:
    #     flash("You need to be logged in to add a console")
    #     return redirect(url_for("get_games"))

    if request.method == "POST":
        console = {
            "console_name": request.form.get("console_name")
        }
        mongo.db.consoles.insert_one(console)
        flash(f"{console['console_name']} Console Successfully Added")
        return redirect(url_for("get_consoles"))

    genres = list(Genre.query.order_by(Genre.genre_name).all())
    return render_template("add_console.html", genres=genres)


@app.route("/edit_console/<_id>", methods=["GET", "POST"])
def edit_console(_id):
    
    console = mongo.db.consoles.find_one({"_id": ObjectId(_id)})

    # if "user" not in session or session["user"] != console["created_by"]:
    #     flash("You can only edit your own consoles!")
    #     return redirect(url_for("get_games"))

    if request.method == "POST":
        submit = {
            "console_name": request.form.get("console_name")
        }
        mongo.db.consoles.update_one({"_id": ObjectId(_id)}, submit)
        return redirect(url_for("get_consoles"))
        flash(f"{console['console_name']} Successfully Updated")

    return render_template("edit_console.html", console=console)


@app.route("/delete_console/<_id>")
def delete_console(_id):

    console = mongo.db.consoles.find_one({"_id": ObjectId(_id)})

    # if "user" not in session or session["user"] != console["created_by"]:
    #     flash("You can only delete your own consoles!")
    #     return redirect(url_for("get_games"))

    # TODO: are you sure you want to delete this console?
    mongo.db.consoles.delete_one({"_id": ObjectId(_id)})
    flash("Console Successfully Deleted")
    return redirect(url_for("get_consoles"))

# GENRE - DB
@app.route("/get_genres")
def get_genres():

    # if "user" not in session or session["user"] != "admin":
    #     flash("You must be admin to manage genres!")
    #     return redirect(url_for("get_games"))

    genres = list(Genre.query.order_by(Genre.genre_name).all())
    games = list(Game.query.all())
    return render_template("genres.html", genres=genres, games=games)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():

    # if "user" not in session or session["user"] != "admin":
    #     flash("You must be admin to manage genres!")
    #     return redirect(url_for("get_games"))

    if request.method == "POST":
        genre = Genre(
            genre_name=request.form.get("genre-name")
        )
        db.session.add(genre)
        db.session.commit()
        return redirect(url_for("get_genres"))
    return render_template("add_genre.html")


@app.route("/edit_genre/<int:genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    # if "user" not in session or session["user"] != "admin":
    #     flash("You must be admin to manage genres!")
    #     return redirect(url_for("get_games"))
    
    genre = Genre.query.get_or_404(genre_id)
    if request.method == "POST":
        # TODO: - it should migrate all games under the edited genre to the new genre name
        genre.genre_name = request.form.get("genre_name")
        db.session.commit()
        return redirect(url_for("get_genres"))
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<int:genre_id>")
def delete_genre(genre_id):
    # if session["user"] != "admin":
    #     flash("You must be admin to manage genres!")
    #     return redirect(url_for("get_games"))

    # TODO: - are you sure you want to delete the genre {{ genre.genre_name }} and all its associated games? y/n
    genre = Genre.query.get_or_404(genre_id)
    db.session.delete(genre)
    db.session.commit()
    # mongo.db.consoles.delete_many({"genre_id": str(genre_id)})
    return redirect(url_for("get_genres"))

# USERS - DB
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter(User.email == \
                                           request.form.get("email").lower()).all()
        
        if existing_user:
            flash("This email is already connected to an account")
            return redirect(url_for("register"))
        
        user = User(
            fname=request.form.get("fname").lower(),
            lname=request.form.get("lname").lower(),
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_games", email=session["user"]))

    return render_template("register.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))