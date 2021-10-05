#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR=$1
cat data/txt/*_${YEAR}_*.txt > data/${YEAR}.txt
python module3/filtering.py 'data' $YEAR
wordcloud_cli --text data/${YEAR}_keywords.txt --imagefile data/${YEAR}.png --width 2000 --height 1000
display data/${YEAR}.png
