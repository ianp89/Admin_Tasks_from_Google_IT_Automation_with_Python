#!/usr/bin/env python3

"""with some tweaking, this will take a filename as an arg and replace part of it"""

import sys
import subprocess

open_file = open(sys.argv[1])

for line in open_file:
	old_file_name = line.strip()
	new_file_name = old_file_name.replace(*old_name*, *new_name*)
	subprocess.run(["mv", old_file_name, new_file_name])

open_file.close()
