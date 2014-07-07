# Run from GAE remote API:
# 	{GAE Path}\remote_api_shell.py -s {YourAPPName}.appspot.com
# 	import export_as_csv

import csv
from db_model import MyModel

def exportToCsv(query, csvFileName, delimiter):
	with open(csvFileName, 'wb') as csvFile:
		csvWriter = csv.writer(csvFile, delimiter=delimiter, quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writeHeader(csvWriter)

		rowsPerQuery = 1000
		totalRowsSaved = 0
		cursor = None
		areMoreRows = True

		while areMoreRows:
			if cursor is not None:
				query.with_cursor(cursor)
			items = query.fetch(rowsPerQuery)
			cursor = query.cursor()

			currentRows =0
			for item in items:
				saveItem(csvWriter, item)
				currentRows += 1

			totalRowsSaved += currentRows
			areMoreRows = currentRows >= rowsPerQuery
			print 'Saved ' + str(totalRowsSaved) + ' rows'

		print 'Finished saving all rows.'

def writeHeader(csvWriter):
	csvWriter.writerow(['Property1', 'Property2', 'Property3']) #Output csv header

def saveItem(csvWriter, item):
	csvWriter.writerow([item.property1, item.property2, item.property3]) # Save items in preferred format


query = MyModel.gql("ORDER BY property1") #Query for items
exportToCsv(query, 'myExport.csv', ',')
