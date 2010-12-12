#!/bin/bash
PATH=/usr/bin/*
yol="/usr/bin/"
for f in $PATH; do
	i=$((${#f}-${#yol}))
	if [ $i -le 3 ]; then
		echo $f
	fi
done
