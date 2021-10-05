"""Iterate over sentences to build word2vec model"""

import logging
import sys

from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec

import nltk
from nltk.tokenize import wordpunct_tokenize

nltk.data.path.append("/home/max/nltk_data")

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    """Tokenize and Lemmatize sentences"""
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for line in open(self.filename, encoding='utf-8', errors="backslashreplace"):
            yield [w.lower() for w in wordpunct_tokenize(line)]

infile = f"data/sents.txt"
sentences = MySentences(infile)
phrases = Phrases(sentences)
bigram = Phraser(phrases)
trigram = Phrases(bigram[sentences])
corpus = list(trigram[bigram[sentences]])
model = Word2Vec(corpus, vector_size=32, window=5, min_count=5, workers=4, epochs=5)
outfile = f"data/bulletins.model"
model.save(outfile)
