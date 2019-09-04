import csv

with open('teacher.csv', 'a') as csvfile:
	fieldnames = ['first_name', 'last_name', 'topic']
	teachwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)	
	teachwriter.writeheader()
	teachwriter.writerow({
		'first_name':'Arjun',
		'last_name':'Sharma',
		'topic':'Python'
	})
	
	teachwriter.writerow({
		'first_name':'Meryl',
		'last_name':'Streep',
		'topic':'Python Advanced'
	})