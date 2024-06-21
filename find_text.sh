#/bin/bash

"""With some tweaking, this will output a list of matching items to a new file"""

>oldFiles.txt

some_files=$(grep ' *variable* ' /home/*user*/Documents/*file* | cut -d ' ' -f *x*)

for file in $some_files; do
	echo "/home/something$file">>oldFiles.txt;
done
