from google.appengine.ext import db

class MyModel(db.Model):
	property1 = db.StringProperty()
	property2 = db.DateTimeProperty()
	property3 = db.IntegerProperty() 