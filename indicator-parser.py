import csv, sqlite3

# Connect to database
dbPath = '/var/www/html/scouse-cameron/phe-data.sqlite'
conn = sqlite3.connect(dbPath, isolation_level=None)
c = conn.cursor()

# Already committed 9/11/15
# with open('indicator-types.csv','rb') as csvfile:
# 	reader = csv.reader(csvfile, delimiter=',',quotechar='"')
# 	for i, row in enumerate(reader):
# 		data = (row[0],)
# 		c.execute('INSERT INTO IndicatorTypes VALUES(NULL,?)',data)

# Already committed 9/11/15
# with open('parent-types.csv','rb') as csvfile:
# 	reader = csv.reader(csvfile, delimiter=',',quotechar='"')
# 	for i, row in enumerate(reader):
# 		data = (row[0],row[1])
# 		c.execute('INSERT INTO ParentTypes VALUES(NULL,?,?)',data)

# with open('area-types.csv','rb') as csvfile:
# 	reader = csv.reader(csvfile, delimiter=',',quotechar='"')
# 	for i, row in enumerate(reader):
# 		data = (row[0],row[1])
# 		c.execute('INSERT INTO AreaTypes VALUES(NULL,?,?)',data)

# Finishing up
conn.commit()
conn.close()