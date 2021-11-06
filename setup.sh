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
source stackviz.py >>~/.gdbinit




