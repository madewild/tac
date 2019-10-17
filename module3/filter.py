"""Filter out stopwords for word cloud"""

import nltk
from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout", 
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu"]
sw = set(sw)

path = "data/txt/1919.txt"
output = open("module3/1919_keywords.txt", "w")

with open(path) as f:
    text = f.read()
    words = nltk.wordpunct_tokenize(text)
    kept = [w.lower() for w in words if len(w) > 2 and w.isalpha() and w.lower() not in sw]
    kept_string = " ".join(kept)
    output.write(kept_string)
