"""Unsupervised clustering example adapted from https://nlpforhackers.io/recipe-text-clustering/"""

import collections
import os
import string
import sys

from nltk import word_tokenize
from nltk.corpus import stopwords
from pprint import pprint
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
  
def process_text(text, stem=True):
    """ Tokenize text and remove punctuation """
    text = text.translate(string.punctuation)
    tokens = word_tokenize(text)
    return tokens
 
def cluster_texts(files, clusters):
    """ Transform texts to Tf-Idf coordinates and cluster texts using K-Means """
    texts = [open(data_path + f).read() for f in files]
    vectorizer = TfidfVectorizer(tokenizer=process_text,
                                 stop_words=stopwords.words('french'),
                                 max_df=0.5,
                                 min_df=0.1,
                                 lowercase=True)
 
    tfidf_model = vectorizer.fit_transform(texts)
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(tfidf_model)
    clustering = collections.defaultdict(list)
 
    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(files[idx])
 
    return clustering
 
if __name__ == "__main__":
    data_path = "data/txt/"
    decade = sys.argv[1]
    files = [f for f in sorted(os.listdir(data_path)) if f"_{decade[:-1]}" in f]
    print(f"{len(files)} documents to cluster for decade {decade}")
    clusters = cluster_texts(files, 10)
    pprint(dict(clusters))
