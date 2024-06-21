#!/usr/bin/env python3

"""This script takes a csv file of a certain format, and turns it into a list of dictionaries"""
"""This allows basic processing, and generates a simple report"""

import csv

#Turn CSV to a list of dicts (DictReader Object):
def read_file(csv_file):
	with open(csv_file) as file:
	csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
	csv_element = csv.DictReader(file, dialect='empDialect')
	element1_list = []
	for element1 in csv_element:
		element1_list.append(element1)
	return element1_list

#Initialize list of dicts counting number element1 per element2
def process_data(element1_list):
	element2_list = []
	for element1 in element1_list:
		element2_list.append(element1['Element2'])
	element2_data = {}
	for element2 in set(element2_list):
		element2_data[element2] = element2_list.count(element2)
	return element2_data

#Generate simply formatted report taking "processed" list, printing key: value per line
def write_report(dictionary, report):
	with open(report, "w+") as file:
		for kee in sorted(dictionary):
			file.write(str(kee) + ": " + str(dictionary[kee]) + "\n")
		file.close()


