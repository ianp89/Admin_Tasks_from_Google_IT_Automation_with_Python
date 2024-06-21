#!/usr/bin/env python3

import sys, os, re

#Inputs a log file, and locates specific errors by name
def error_search(log_file):
	error = input("What error are you looking for?")
	returned_errors = []
	with open(log_file, mode='r', encoding='UTF-8') as file:
		for log in file.readlines():
			error_patterns = ["error"]
			for i in range(len(error.split(' '))):
				error_patterns.append(r'{}'.format(error.split(' ')[i].lower()))
			if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
				returned_errors.append(log)
		file.close()
	return returned_error

#Create new file with logs specified in previous function
def file_output(returned_errors):
	with open((os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
		for error in returned_errors:
			file.write(error)
		file.close()

#First verify paramenter as valid log file, then executes two above functions, creating the actual file specified in the previous function
if __name__ == "__main__":
	log_file = sys.argv[1]
	returned_errors = error_search(log_file)
	file_output(returned_errors)
	sys.exit(0)

