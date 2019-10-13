"""Analyse frequency distribution of words"""

import nltk
from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout", 
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu"]
sw = set(sw)
print(f"{len(sw)} stopwords used: {sorted(sw)}")

path = "data/txt/all.txt"
limit = 10**8

with open(path) as f:
    text = f.read()[:limit]
    words = nltk.wordpunct_tokenize(text)
    print(f"{len(words)} words found")
    kept = [w.lower() for w in words if len(w) > 2 and w.isalpha() and w.lower() not in sw]
    voc = set(kept)
    print(f"{len(kept)} words kept ({len(voc)} different word forms)")
    fdist = nltk.FreqDist(kept)
    print(fdist.most_common(50))
    fdist.plot(50, cumulative=True)
    print(fdist.hapaxes())
    long_words = [w for w in voc if len(w) > 15]
    print(sorted(long_words))
