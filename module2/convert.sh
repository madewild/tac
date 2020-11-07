#!/usr/bin/env bash

# Converting PDFs to text files and moving them to a new directory

for file in /Volumes/Macintosh HD/Data/ADB/pdf/*.pdf; do pdftotext "$file" "${file%.*}.txt"; done
mkdir /Volumes/Macintosh HD/Data/txt
mv /Volumes/Macintosh HD/Data/ADB/pdf/pdf/*.txt /Volumes/Macintosh HD/Data/ADB/pdf/txt/
ls /Volumes/Macintosh HD/Data/ADB/pdf/txt | wc -l
cat /Volumes/Macintosh HD/Data/ADB/pdf/txt/*.txt > /Volumes/Macintosh HD/Data/ADB/pdf/all.txt
wc /Volumes/Macintosh HD/Data/ADB/pdf/all.txt
