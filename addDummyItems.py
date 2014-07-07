import webapp2
import datetime
from db_model import MyModel

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		numItemsToSave = 100
		for i in range(0,numItemsToSave):
			item = MyModel(property1='value' + str(i), property2=datetime.datetime.now(), property3=i)
			item.put()
		self.response.write('Saved ' + str(numItemsToSave) + ' items')

application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)