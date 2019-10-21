"""Testing keyword extraction with YAKE"""

import os
import yake

ignored = set(["conseil communal", "conseil général"])

kw_extractor = yake.KeywordExtractor(lan="fr", top=20)
data_path = "data/txt/"
files = os.listdir(data_path)
for f in sorted(files):
    if f.startswith("Bxl_"):
        text = open(data_path + f).read()
        keywords = kw_extractor.extract_keywords(text)
        kept = []
        for score, kw in keywords:
            words = kw.split()
            if len(words) > 1 and kw not in ignored:
                kept.append(kw)
        print(f"{f} mentions these keywords: {', '.join(kept)}...")
