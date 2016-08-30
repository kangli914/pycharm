#!/bin/bash

tmpdir="tmp/fr-logrotator-plugin"
rm $tmpdir/request.log

for f in logs/abruzzo/FusionReactor/20160725/*.zip
do
	echo "Processing $f file..."
	# unzip logs/abruzzo/FusionReactor/20160724/1a66746d-42d4-4a08-9d79-a2d212c53b74.zip fr-logrotator-plugin/request.log -d tmp/
	unzip $f fr-logrotator-plugin/request.log -d tmp/
	
	srcfile="request.log"
	fileword=$(head -n1 $tmpdir/$srcfile | awk '{print $1, $2}');
	date=$(echo $fileword | awk '{print $1}')
	hr=$(echo $fileword | cut -f2 -d" " | cut -f1 -d":")
	min=$(echo $fileword | cut -f2 -d" " | cut -f2 -d":")
	trgfile=$date"_"$hr$min

	# Everything after first dot is considered as extention
	ext=$(echo $srcfile | sed 's/.*\.\(.*\)/.\1/g')
	prefix=$(echo $srcfile | cut -f1 -d".")
	trgfile=$prefix"_"$trgfile$ext
	[ "$srcfile" != "$fileword" ] && $(cp "$tmpdir/$srcfile" "$tmpdir/$trgfile")
	
	rm $tmpdir/$srcfile
done
