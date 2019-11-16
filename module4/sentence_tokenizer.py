"""Tokenize sentences"""

import os
import sys
import nltk
from nltk.tokenize import sent_tokenize

nltk.data.path.append("/home/max/nltk_data")

infile = f"data/all.txt"
outfile = f"data/sents.txt"

with open(outfile, 'w', encoding="utf-8") as output:
    with open(infile, encoding="utf-8", errors="backslashreplace") as f:
        for line in f:
            sentences = sent_tokenize(line)
            for sent in sentences:
                output.write(sent + "\n")
