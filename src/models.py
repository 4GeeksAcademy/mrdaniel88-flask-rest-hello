from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    homeworld = db.Column(db.Integer, db.ForeignKey("planets.id"))
    mass = db.Column(db.Integer, nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    #species = db.Column(db.String(250), db.ForeignKey("species.id"))
    starships = db.Column(db.String(250))
    vehicles = db.Column(db.String(250), nullable=False)
    planet = db.relationship("Planets")
    #user = db.relationship("Favorites")
    #specie = db.relationship("Species")

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "name":self.name,
            "birth_year":self.birth_year,
            "gender":self.gender
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    films = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    residents = db.Column(db.String(250), nullable=False)
    roation_period = db.Column(db.Integer, nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    #user = db.relationship("Favorites")

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "name":self.name,
            "climate":self.climate,
            "gravity":self.gravity
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
    element_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User)

    def __repr__(self):
        return '<Favorites %r>' % self.type % self.element_id
    
    def serialize(self):
        return {
            "type":self.type,
            "element_id":self.element_id,
            "userId":self.user_id
        }