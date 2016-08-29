#!/bin/bash

srcfile="request.log"
fileword=$(head -n1 $srcfile | awk '{print $1, $2}');
date=$(echo $fileword | awk '{print $1}')
hr=$(echo $fileword | cut -f2 -d" " | cut -f1 -d":")
min=$(echo $fileword | cut -f2 -d" " | cut -f2 -d":")
trgfile=$date"_"$hr$min



# Everything after first dot is considered as extention
ext=$(echo $srcfile | sed 's/.*\.\(.*\)/.\1/g')
prefix=$(echo $srcfile | cut -f1 -d".")
trgfile=$prefix"_"$trgfile$ext
[ "$srcfile" != "$fileword" ] && $(cp "$srcfile" "$trgfile")