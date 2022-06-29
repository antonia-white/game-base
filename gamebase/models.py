from gamebase import db

class Game(db.Model):
    # schema for the Game model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=True)
    developer = db.Column(db.String(50))
    release_date = db.Column(db.Date)
    is_singleplayer = db.Column(db.Boolean, default=True, nullable=False)
    image_url = db.Column(db.Text)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"#{self.id} - Title: {self.title} | Singleplayer: {self.is_singleplayer}"


class Genre(db.Model):
    # schema for the Genre model
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(50), nullable=False)
    games = db.relationship("Game", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return self