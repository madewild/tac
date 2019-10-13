"""Exploring the corpus"""

from collections import defaultdict
import os

import matplotlib.pyplot as plt
import numpy as np

path = "data/txt/"
dic = defaultdict(int)
files = sorted(os.listdir(path))

for f in files:
    if "_" in f:
        elems = f.split("_")
        city = elems[0]
        year = elems[1]
        tome = elems[3]
        decade = year[:3] + "0"
        dic[city] += 1
        dic[decade] += 1
        dic[tome] += 1

    else:
        print(f"Anomalous file: {f}")

print(f"There are {dic['Bxl']} bulletins from Brussels and {dic['Lkn']} from Laeken")
nb_rap = dic['RptAn']
print(f"{len(files)-nb_rap-1} are real bulletins and {nb_rap} are annual reports")

def plot_bar():
    index = np.arange(len(dic))
    plt.bar(index, dic.values())
    plt.xlabel('Décennie', fontsize=5)
    plt.ylabel('# bulletins', fontsize=5)
    plt.xticks(index, dic.keys(), fontsize=5, rotation=30)
    plt.title('Évolution du nombre de bulletins')
    plt.show()

#plot_bar()
