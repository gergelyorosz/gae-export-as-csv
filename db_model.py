from google.appengine.ext import db

class MySong(db.Model):
	name = db.StringProperty()
	artist = db.StringProperty()
	releaseDate = db.DateTimeProperty()
	numAwards = db.IntegerProperty() 