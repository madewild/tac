"""Detect languages used in bulletins"""

import os
from collections import defaultdict

import langid
langid.set_languages(['fr', 'nl']) # restricting to these two languages only to prevent weird results

lang_dict = defaultdict(int)

root = "data/txt/"
txts = os.listdir(root)
print(f"{len(txts)} TXT files found")

for txt in txts:
    text = open(os.path.join(root, txt)).read()
    text_length = len(text)
    if text_length > 10:
        lang, conf = langid.classify(text)
        lang_dict[lang] += 1
    else:
        print(f"{txt} contains only {text_length} characters, treating as unknown")
        lang_dict['n/a'] += 1

for k, v in lang_dict.items():
    print(f"{k}\t{v}")
