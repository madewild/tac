"""Exploring the corpus"""

from collections import defaultdict
import os

import matplotlib.pyplot as plt
import numpy as np

path = "data/txt/"
dic = defaultdict(int)
files = sorted(os.listdir(path))
print(files[:10])

for f in files:
    if "_" in f:
        year = f.split("_")[1]
        decade = year[:3] + "0"
        dic[decade] += 1
    else:
        print(f"Anomalous file: {f}")

def plot_bar():
    index = np.arange(len(dic))
    plt.bar(index, dic.values())
    plt.xlabel('Décennie', fontsize=5)
    plt.ylabel('# bulletins', fontsize=5)
    plt.xticks(index, dic.keys(), fontsize=5, rotation=30)
    plt.title('Nombre de bulletins par décennie')
    plt.show()

plot_bar()