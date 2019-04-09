#Quais são as profissões em que mais pessoas tem ganho anual $ 50K? Quais profissões tem mais de $ 50K?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 12})

atributos = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',  'relationship', 'race', 'sex', 'capital_gain',  'capital-loss', 'hours-per-week', 'native-country', 'class_']

adult = pd.read_csv('adult.data', names = atributos, delimiter = ',')

rel = adult.groupby(['occupation', 'class_'])['occupation'].count()

menor_igual = []
maior = []

valores = rel.tolist()

for i in range(0, len(valores), 2):
	menor_igual.append(valores[i])
	maior.append(valores[i  + 1])

indices = []

for i in range(0, len(rel.index), 2):
	indices.append(rel.index[i][0])

df = pd.DataFrame({'<=50K': menor_igual, '>50K': maior}, index = indices)

ax = df.plot.bar(rot=0)
plt.ylim(top=4000)
for p in ax.patches[0:]:
	h = p.get_height()
	x = p.get_x()+p.get_width()/2.
	if h != 0:
		ax.annotate("%g" % p.get_height(), xy=(x,h), xytext=(0,4), textcoords="offset points", ha="center", va="bottom", rotation = 90)

plt.subplots_adjust(left=0.05, bottom=0.25, right=0.99, top=0.99, wspace=0.20, hspace=0.20)
ax.yaxis.grid(True)
plt.xticks(rotation = 'vertical')
plt.show()
