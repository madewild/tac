"""Supervised classification example"""

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import seaborn as sn

from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

news = fetch_20newsgroups(subset='all')

print("Number of articles: " + str(len(news.data)))
print("Number of categories: " + str(len(news.target_names)))

labels = news.target_names

classifier = Pipeline([ ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english'))),('classifier', MultinomialNB())])
X_train, X_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.2, random_state=11)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred, target_names=labels))
conf_mat = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(15, 10))
sn.heatmap(conf_mat, annot=True, fmt="d", xticklabels=labels, yticklabels=labels)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()
