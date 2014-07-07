import csv
from db_model import User, Song, UserSong, UserSongRecommendation, UserSavedList

def exportToCsv(query, csvFileName, delimiter):
	with open(csvFileName, 'wb') as csvFile:
		csvWriter = csv.writer(csvFile, delimiter=delimiter, quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writeHeader(csvWriter)

		rowsPerQuery = 1
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

def writeHeader(csvWriter)
	csvWriter.writerow(['Email', 'User ID', 'Date Saved']) #Output csv header

def saveItem(csvWriter, item):
	csvWriter.writerow([item.email, item.userId, item.dateSaved]) # Save items in preferred format


query = UserSavedList.gql("ORDER BY email") #Query for items
exportToCsv(query, 'testCsv.csv', ',')
