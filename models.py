from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Show(db.Model):
  __tablename__ = 'show'

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)

class Venue(db.Model):
  __tablename__ = 'venue'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String()))
  website_link = db.Column(db.String(500))
  seeking_talent = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.Text)
  shows = db.relationship('Show', backref='venue', lazy=True, cascade='all, delete-orphan')
  created_on = db.Column(db.DateTime, default=datetime.utcnow)

  @property 
  def upcoming_shows(self):
    upcoming_shows = [show for show in self.shows if show.start_time > datetime.now()]
    return upcoming_shows
  
  @property
  def num_upcoming_shows(self):
    return len(self.upcoming_shows)
  
  @property
  def past_shows(self):
    past_shows = [show for show in self.shows if show.start_time < datetime.now()]
    return past_shows
  
  @property
  def num_past_shows(self):
    return len(self.past_shows)


  # implement any missing fields, as a database migration using
  # Flask-Migrate


class Artist(db.Model):
  __tablename__ = 'artist'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String(120)))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  website_link = db.Column(db.String(120))
  seeking_venue = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.Text)
  shows = db.relationship('Show', backref='artist', lazy=True)
  created_on = db.Column(db.DateTime, default=datetime.utcnow)

  @property
  def upcoming_shows(self):
    upcoming_shows = [show for show in self.shows if show.start_time > datetime.now()]
    return upcoming_shows
    
  @property
  def num_upcoming_shows(self):      
    return len(self.upcoming_shows)
      
  @property
  def past_shows(self):
    past_shows = [show for show in self.shows if show.start_time < datetime.now()]
    
    return past_shows
    
  @property
  def num_past_shows(self):
    return len(self.past_shows)


  # implement any missing fields, as a database migration using
  # Flask-Migrate

# Implement Show and Artist models, and complete all model
# relationships and properties, as a database migration.
