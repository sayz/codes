#!/bin/bash

PATH=/usr/bin/*


for f in $PATH; do
	if [ -x $f ]; then
		echo "executable-->$f"
	fi
	if [ -h $f ]; then
		echo "symbolic-->$f"
	fi
done












