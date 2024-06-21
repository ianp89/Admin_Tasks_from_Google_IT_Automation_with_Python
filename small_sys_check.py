#!/usr/bin/env python3

import shutil, psutil, requests

disk_use = shutil.disk_usage("/")

print("Disk Use Stats: " + str(disk_use))
print("Free Disk Percentage: " + str(disk_use.free/disk_use.total*100))
print("CPU Use Percentage: " + str(psutil.cpu_percent(0.5))

def disk_check(disk):
	du = shutil.disk_usage(disk)
	free_disk = du.free/du.total*100
	return free_disk > 33

def cpu_check():
	cpu_use = psutil.cpu_percent(0.5)
	return cpu_use < 80

if not disk_check("/"):
	print("Memory Use too high!")
if not cpu_check():
	print("CPUR use too high!")
elif disk_check("/") and cpu_check():
	print("All good with memory and CPU. Let's do a quick connectivity check...")

if requests.get("http://www.google.com") != 200:
	print("The connection looks good :)")
else:
	print("There is a connectivity problem!")
