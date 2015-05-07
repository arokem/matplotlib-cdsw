""" load_hp_data.py 

A module for loading data from the Harry Potter wikipedia data set

""" 
import csv
from datetime import datetime

f = open('hp_wiki.tsv', 'r')
reader = csv.DictReader(f, delimiter='\t')

columns = {}
for fieldname in reader.fieldnames:
	columns[fieldname] = []


rows = []
for row in reader:
	# Convert timestamp from a string to a date:
	row['timestamp'] = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
	rows.append(row)
	for fieldname, value in row.items():
		columns[fieldname].append(value)