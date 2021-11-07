#!/bin/bash

echo "building..."

if  ! hash gdb ; then
	echo "Error: Could not find gdb in $PATH"
	exit
else
	
	echo "success | gdb installation found"
fi

if [ -f "~/.gdbinit" ];
then
	echo "success | .gdbinit file found."
else
	touch ~/.gdbinit
	echo "success | .gdbinit created"
fi
#echo "source gdb_stackviz/stackviz.py" >> ~/.gdbinit # Runs the proper file for execution. If this is inserted into .gdbinit, it will always start.

# UNAME=$(uname -m)
# if ![[ UNAME = "x86-64" ]] ;then
#	string manipulate our python file.
# 	sed -i 's/esp/rsp/g' ./gdb_stackviz/stackviz.py #stack pointer variable for Arm systems go here. If they have an alt system. They can edit the python file themselves
# 	rm check.txt
# fi
if  ! grep -q "source gdb_stackviz/stackviz.py" ~/.gdbinit;then #checks to see if the string already exists in .gdbinit. If it does DON'T DO IT AGAIN!!
	echo "source ./gdb_stackviz/stackviz.py" >> ~/.gdbinit
	echo "success | configured starting script" 
else
	echo "success | already configured"
fi

echo "config successfully completed"
