from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import enum

# enum for genres
class Genre(enum.Enum):
  Alternative = 'Alternative'
  Blues = 'Blues'
  Classical = 'Classical'
  Country = 'Country'
  Electronic = 'Electronic'
  Folk = 'Folk'
  Funk = 'Funk'
  HipHop = 'Hip-Hop'
  HeavyMetal = 'Heavy Metal'
  Instrumental = 'Instrumental'
  Jazz = 'Jazz'
  MusicalTheatre = 'Musical Theatre'
  Pop = 'Pop'
  Punk = 'Punk'
  RnB = 'R&B'
  Reggae = 'Reggae'
  RocknRoll = 'Rock n Roll'
  Soul = 'Soul'
  Other = 'Other'

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Venue(db.Model):
  __tablename__ = 'Venue'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  genres = db.Column(db.Enum(Genre))
  website_link = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.Text)

  # TODO: implement any missing fields, as a database migration using
  # Flask-Migrate


class Artist(db.Model):
  __tablename__ = 'Artist'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))

  # TODO: implement any missing fields, as a database migration using
  # Flask-Migrate

class Show(db.Model):
  __tablename__ = 'Show'
  id = db.Column(db.Integer, primary_key=True)

# TODO Implement Show and Artist models, and complete all model
# relationships and properties, as a database migration.
