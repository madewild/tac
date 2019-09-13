""" Iterate sentences to build word2vec model """

import logging
import sys

from gensim.models.phrases import Phrases, Phraser
from gensim.models.word2vec import Word2Vec

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize

wnl = WordNetLemmatizer()

nltk.data.path.append("/srv/resources/nltk_data")

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    '''Tokenize and Lemmatize sentences'''
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for line in open(self.filename, encoding='utf-8', errors="backslashreplace"):
            yield [w.lower() for w in wordpunct_tokenize(line)]

prog = sys.argv[1]
infile = f"data/{prog}_sents.txt"
sentences = MySentences(infile)
phrases = Phrases(sentences)
bigram = Phraser(phrases)
trigram = Phrases(bigram[sentences])
quadrigram = Phrases(trigram[bigram[sentences]])
corpus = list(quadrigram[trigram[bigram[sentences]]])
model = Word2Vec(corpus, size=32, window=5, min_count=5, workers=4, iter=5)
outfile = f"data/{prog}.model"
model.save(outfile)
