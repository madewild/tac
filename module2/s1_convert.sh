#!/usr/bin/env bash

# Converting PDFs to text files and moving them to a new directory

for file in data/pdf/*.pdf; do pdftotext -enc UTF-8 "$file" "${file%.*}.txt"; done
mkdir data/txt
mv data/pdf/*.txt data/txt/
ls data/txt | wc -l
cat data/txt/*.txt > data/all.txt
wc data/all.txt
