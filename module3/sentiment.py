"""Sentiment analysis with Textblob-FR"""

import sys

from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

input_text = sys.argv[1]
blob = tb(input_text)
pola, subj = blob.sentiment
perc = f"{100*abs(pola):.0f}"
if pola > 0:
    sent = f"{perc}% positive"
elif pola < 0:
    sent = f"{perc} negative"
else:
    sent = "neutral"
if subj > 0:
    fact = f"{100*subj:.0f}% subjective"
else:
    fact = "perfectly objective"
print(f"This text is {sent} and {fact}.")
