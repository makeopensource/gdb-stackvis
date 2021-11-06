#!/bin/bash

echo "Building"

if  ! hash gdb ; then
	echo "Could not find gdb in $PATH"
	exit
else
	echo "An instillation of gdb was found"
fi

if [ -f "~/.gdbinit" ];
then
	echo ".gdbinit file found."
else
	touch ~/.gdbinit
fi
echo "source gdb-stackvis/stackvis.py" >> ~/.gdbinit # Runs the proper file for execution. If this is inserted into .gdbinit, it will always start.
echo "DONE DO NOT RUN THIS .sh FILE AGAIN. YOU CAN SAFELY DELETE THIS FILE."
