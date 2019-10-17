"""Sentiment analysis with Textblob-FR"""

from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

blob1 = tb(u"Quelle belle matinée")
blob1.sentiment
