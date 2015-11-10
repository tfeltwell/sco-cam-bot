import csv, sqlite3

# Connect to database
dbPath = '/var/www/html/scouse-cameron/phe-data.sqlite'
conn = sqlite3.connect(dbPath, isolation_level=None)
c = conn.cursor()

def getIndicatorByName(indName):
	data = (indName,)
	c.execute('SELECT key FROM IndicatorTypes WHERE name=?',data)
	result = c.fetchone()
	return result[0]

def getAreaByCode(pheCode):
	data = (pheCode,)
	c.execute('SELECT key FROM AreaTypes WHERE phe_code=?',data)
	result = c.fetchone()
	return result[0]

def getParentByCode(pheCode):
	data = (pheCode,)
	c.execute('SELECT key FROM ParentTypes WHERE phe_code=?',data)
	result = c.fetchone()
	return result[0]


# getAreaByCode('E06000001')
# getParentByCode('E12000007')

with open('district-stats.csv','rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',',quotechar='"')
	for i, row in enumerate(reader):
		data = (getIndicatorByName(row[0]),row[1],getParentByCode(row[2]),getAreaByCode(row[3]),row[4],row[5],row[6],row[7],row[8],row[9],row[10])
		c.execute('INSERT INTO Data VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?)',data)
		print 'Inserted',str(i)
print 'Finished'
		


