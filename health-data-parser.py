import csv

with open('district-stats.csv','rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',',quotechar='"')
	for row in reader:
		print ', '.join(row)