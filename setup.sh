#!/bin/bash

echo "Building"

if  ! hash gdb ; then
	echo "Could not find gdb in $PATH"
	exit
else
	
	echo "gdb instillation found!"
fi

if [ -f "~/.gdbinit" ];
then
	echo ".gdbinit file found."
else
	touch ~/.gdbinit
fi
#echo "source gdb_stackviz/stackviz.py" >> ~/.gdbinit # Runs the proper file for execution. If this is inserted into .gdbinit, it will always start.

uname -m > check.txt
if ! grep -q "x86-64" check.txt;then
	#string manipulate our python file.
	sed -i 's/esp/rsp/g' ./gdb_stackviz/stackviz.py #stack pointer variable for Arm systems go here. If they have an alt system. They can edit the python file themselves
	rm check.txt
fi
if  ! grep -q "source gdb_stackviz/stackviz.py" ~/.gdbinit;then #checks to see if the string already exists in .gdbinit. If it does DON'T DO IT AGAIN!!
	echo "source ./gdb_stackviz/stackviz.py" >> ~/.gdbinit 
else
	echo "Already configured!"
fi
