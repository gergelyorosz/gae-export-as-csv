gae-export-as-csv
=================

#Google App Engine CSV Exporter

A utility script that allows saving / backing up / exporting Google App Engine datastore data in a csv format. This script is capable downloading large quantities of data, not being bound by the GAE request quotas. 

#Why

GAE does not have a built in mechanism of backing up / exporting data in a portable format. The [DataStore Admin](https://developers.google.com/appengine/docs/adminconsole/datastoreadmin#backing_up_data) currently only allows backing up to blobstore or Google Cloud Storage. 

For a project I was working on I wanted something simpler - and for smaller data sets what could beats having the data avaialble as good ol' text based csv files.

#Usage
Configure and run The script is `export_as_csv.py` in the GAE Remote API shell.
##Environment
The script needs to be run from the [GAE Remote API shell] (https://developers.google.com/appengine/docs/python/tools/remoteapi). Follow setup (including enabling remote_api on the datastore) as described there.
##Configuration
Configure `export_as_csv.py` so that it fetches the table and columns you want. To do so, change the following lines in it:
```python
def writeHeader(csvWriter)
	csvWriter.writerow(['Email', 'User ID', 'Date Saved']) #Output csv header

def saveItem(csvWriter, item):
	csvWriter.writerow([item.email, item.userId, item.dateSaved]) # Save items in preferred format
```

Create a custom query and invoke the exportToCsv method, passing the query, filename and delimiter:

```python
query = UserSavedList.gql("ORDER BY email") #Query for items
exportToCsv(query, 'testCsv.csv', ',')
```

#Example

The source code contains an example application. The application creates `MyModel` rows and the `export_as_csv.py` downloads these.
