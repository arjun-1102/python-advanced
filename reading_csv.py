import csv

#with open('test.csv', newline="") as csvfile:
#	cust_reader = csv.reader(csvfile, delimiter=",")
#	rows = list(cust_reader)
#	for row in rows[:2]:
#		print(', '.join(row))
		
with open('test.csv', newline="") as csvfile:
	cust_reader = csv.DictReader(csvfile, delimiter=",")
	rows = list(cust_reader)
	for row in rows[1:10]:
		print(row['Email'])
		