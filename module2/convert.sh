#!/usr/bin/env bash

# Converting PDFs to text files and moving them to a new directory

for file in data/pdf/*.pdf; do pdftotext "$file" "${file%.*}.txt"; done
mkdir data/txt
mv data/pdf/*.txt data/txt/
