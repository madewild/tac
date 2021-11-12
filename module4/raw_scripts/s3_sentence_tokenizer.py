"""Tokenize sentences"""

import nltk
from nltk.tokenize import sent_tokenize

nltk.data.path.append("/home/max/nltk_data")

infile = "data/oneliner.txt"
outfile = "data/sents.txt"

with open(outfile, 'w', encoding="utf-8") as output:
    with open(infile, encoding="utf-8", errors="backslashreplace") as f:
        for line in f:
            sentences = sent_tokenize(line)
            for sent in sentences:
                output.write(sent + "\n")
