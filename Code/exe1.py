#Observe a relação existente entre gênero e estado civil. Descreva suas observações. Lembre-se que a base de dados Adult é uma amostra com apenas maiores de idade (age > 16) e que trabalham (hours-per-week > 0);

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 12})

atributos = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',  'relationship', 'race', 'sex', 'capital-gain',  'capital-loss', 'hours-per-week', 'native-country', 'class']

adult = pd.read_csv('adult.data', names=atributos, delimiter=',')

rel = adult[['sex', 'marital-status']]

rel = rel.groupby(['marital-status', 'sex'])['marital-status'].count()

female = []
male = []

valores = rel.tolist()

for i in range(0, len(valores), 2):
	female.append(valores[i])
	male.append(valores[i  + 1])

indices = []

for i in range(0, len(rel.index), 2):
	indices.append(rel.index[i][0])

df = pd.DataFrame({'Female': female, 'Male': male}, index = indices)

ax = df.plot.bar(rot = 0)

ax.yaxis.grid(True)
for p in ax.patches[0:]:
	h = p.get_height()
	x = p.get_x()+p.get_width()/2.
	if h != 0:
		ax.annotate("%g" % p.get_height(), xy=(x,h), xytext=(0,4), textcoords="offset points", ha="center", va="bottom")
plt.subplots_adjust(left = 0.05, bottom = 0.05, right =0.99, top=0.99, wspace=0.20, hspace=0.20)
plt.show()
