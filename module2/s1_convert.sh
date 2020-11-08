#!/usr/bin/env bash

# Converting PDFs to text files and moving them to a new directory

for file in /Volumes/Macintosh\ HD/Data/ADB/pdf/*.pdf; do pdftotext -enc UTF-8 "$file" "${file%.*}.txt"; done
mkdir /Volumes/Macintosh\ HD/Data/ADB/txt
mv /Volumes/Macintosh\ HD/Data/ADB/pdf/*.txt /Volumes/Macintosh\ HD/Data/ADB/txt/
ls /Volumes/Macintosh\ HD/Data/ADB/txt | wc -l
cat /Volumes/Macintosh\ HD/Data/ADB/txt/*.txt > /Volumes/Macintosh\ HD/Data/ADB/all.txt
wc /Volumes/Macintosh\ HD/Data/ADB/all.txt
