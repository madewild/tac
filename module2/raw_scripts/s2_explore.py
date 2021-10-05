"""Exploring the corpus"""

from collections import defaultdict
import os

import matplotlib.pyplot as plt
import numpy as np

path = "data/txt/"
dic = defaultdict(int)
dic2 = defaultdict(int)
all_years = [str(year) for year in range(1847, 1979)]
covered_years = set()

files = sorted(os.listdir(path))
for f in files:
    if "_" in f:
        elems = f.split("_")
        city = elems[0]
        year = elems[1]
        tome = elems[3]
        covered_years.add(year)
        decade = year[:3] + "0s"
        dic[decade] += 1
        dic2[city] += 1
        dic2[tome] += 1
    else:
        print(f"Anomalous file: {f}")

print(f"There are {dic2['Bxl']} bulletins from Brussels and {dic2['Lkn']} from Laeken")
nb_rap = dic2['RptAn']
print(f"{len(files)-nb_rap-1} are real bulletins and {nb_rap} are annual reports")
missing_years = [y for y in all_years if y not in covered_years]
print(f"Missing years: {', '.join(missing_years)}")

def plot_bar():
    index = np.arange(len(dic))
    plt.bar(index, dic.values())
    plt.xlabel('Décennie')
    plt.ylabel('# bulletins')
    plt.xticks(index, dic.keys(), fontsize=8, rotation=30)
    plt.title('Évolution du nombre de bulletins')
    plt.show()

plot_bar()
