import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

atributos = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital-status', 'occupation',  'relationship', 'race', 'sex', 'capital_gain',  'capital-loss', 'hours-per-week', 'native-country', 'class_']

adult = pd.read_csv('adult.data', names = atributos, delimiter = ',')

rel = adult.groupby(['education', 'class_'])['education'].count()

menor_igual = []
maior = []

valores = rel.tolist()

valores.insert(27, 0)

for i in range(0, len(valores), 2):

	perc = 1 / (valores[i] + valores[i + 1])
	menor_igual.append(valores[i] * perc)
	maior.append(valores[i + 1] * perc)

print(menor_igual)
print(maior)

indices = []

for i in range(0, len(rel.index), 2):
	indices.append(rel.index[i][0])

df = pd.DataFrame({'<=50K': menor_igual, '>50K': maior}, index = indices)

ax = df.plot.bar(rot = 0, stacked = True)

#for p in ax.patches:
#    ax.annotate("%.2f" % p.get_height(), xy = (p.get_x(), p.get_y()), textcoords="offset points", ha="center", va="bottom")

plt.subplots_adjust(left=0.05, bottom=0.17, right=0.99, top=0.99, wspace=0.20, hspace=0.20)
ax.yaxis.grid(True)

plt.xticks(rotation='vertical')

plt.show()
