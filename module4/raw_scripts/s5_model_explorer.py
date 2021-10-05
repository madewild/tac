"""Playing with word2vec model"""

from pprint import pprint
from gensim.models import Word2Vec

model = Word2Vec.load("data/bulletins.model")

word1 = "boucher"
pprint(model.wv[word1])

word2 = "fleuriste"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

word2 = "boulanger"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

pprint(model.wv.most_similar("kermesse", topn=3))

pprint(model.wv.most_similar("bruxelles"))

pprint(model.wv.most_similar(positive=['bruxelles', 'france'], negative=['belgique']))
