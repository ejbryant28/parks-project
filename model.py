
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    """Users model"""

    __tablename__="users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    #add username uniqueness constraint

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<User username = {} name = {} email = {}>".format(self.username, self.name, self.email) # pragma: no cover


class Park(db.Model):
    """Parks model"""

    __tablename__ = "parks"

    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    reviews = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Park park_name = {} location = {} date = {}>".format(self.park_name, self.location, self.date) # pragma: no cover


class UserPark(db.Model):
    """An instance of a user searching for a park"""

    user_park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False)
    date_searched = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", backref=db.backref("user_park")) 
    park = db.relationship("Park", backref=db.backref("user_park"))


    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<UserPark user_id = {} park_id = {} date = {}>".format(self.user_id, self.park_id, self.date_searched) # pragma: no cover



def connect_to_db(app, database):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    print("Connected to DB")


if __name__ == "__main__":

    from server import app  # pragma: no cover
    connect_to_db(app, 'postgres:///parks') # pragma: no cover
    db.create_all() # pragma: no cover