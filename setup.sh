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

sudo cp -r gdb_stackviz /usr/bin

if  ! grep -q "source /usr/bin/gdb_stackviz/stackviz.py" ~/.gdbinit;then #checks to see if the string already exists in .gdbinit. If it does DON'T DO IT AGAIN!!
	echo "source /usr/bin/gdb_stackviz/stackviz.py" >> ~/.gdbinit
	echo "success | configured starting script" 
else
	echo "success | already configured"
fi

echo "config successfully completed"
