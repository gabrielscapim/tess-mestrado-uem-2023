#!/bin/sh

#-----------------------------------------
system=luiz
reference="1.01 1.01 1.01 1.01"

echo "\n$system"
FILES=./dados/$system/*
for f in $FILES
do
	echo "Processing $f"
	echo $f >> ./resultado/$system.txt
	./hv-1.3-src/hv -r "$reference" $f >> ./resultado/$system.txt
	echo "\n" >> ./resultado/$system.txt
done



