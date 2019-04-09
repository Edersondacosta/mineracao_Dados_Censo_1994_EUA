#Quem trabalha mais horas em média: o marido, a esposa, pessoas com filhos, etc? Este comportamento varia dependendo da idade?

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
import numpy as np
import heatmap

atributos = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',  'relationship', 'race', 'sex', 'capital_gain',  'capital-loss', 'hours_per_week', 'native-country', 'class_']

adult = pd.read_csv('adult.data', names = atributos, delimiter = ',')

rel = adult[['relationship', 'hours_per_week', 'age']]

s_hours_per_week = adult['hours_per_week']
s_age = adult['age']
s_relationship = adult['relationship']

rel = pd.concat([s_hours_per_week, s_age, s_relationship], axis=1)

rel = rel.sort_values(['relationship', 'hours_per_week', 'age']).astype(str)

for i in range(0, 100, 10):
	for j in range(i+1, (i + 11), 1):
		rel['hours_per_week'].replace(str(j), str(i+1) + '-' + str(i+10), inplace = True)

relationship = preprocessing.LabelEncoder()
relationship.fit(rel['relationship'])
rel['relationship'] = relationship.transform(rel['relationship'])
#['Husband' 'Not-in-family' 'Other-relative' 'Own-child' 'Unmarried' 'Wife']

hours_per_week = preprocessing.LabelEncoder()
hours_per_week.fit(rel['hours_per_week'])
rel['hours_per_week'] = hours_per_week.transform(rel['hours_per_week'])
#['1-10' '11-20' '21-30' '31-40' '41-50' '51-60' '61-70' '71-80' '81-90' '91-100']

'''age = preprocessing.LabelEncoder()
age.fit(rel['age'])
rel['age'] = age.transform(rel['age'])
#['11-20' '21-30' '31-40' '41-50' '51-60' '61-70' '71-80' '81-90']'''

rel = rel.sort_values(['relationship', 'hours_per_week', 'age'])

#rel.drop_duplicates(inplace=True)

#criacao de matriz
vetor1 = rel['hours_per_week'].values
vetor2 = rel['relationship'].values
valores = rel['age'].values

m = len(set(vetor1))
n = len(set(vetor2))

matriz = []

for i in range(0, m, 1):
	aux = []
	for j in range(0, n, 1):
		aux.append(0)
	matriz.append(aux)

for i in range(0, len(valores), 1):
	matriz[vetor1[i]][vetor2[i]] = rel.query('hours_per_week == "' + str(vetor1[i]) + '" & relationship == "' + str(vetor2[i]) + '"')['age'].astype(int).mean()

fig, ax = plt.subplots()

im, cbar = heatmap.heatmap(np.array(matriz), hours_per_week.inverse_transform(np.arange(m)), relationship.inverse_transform(np.arange(n)), ax=ax, cmap="YlGn", cbarlabel="average age")
texts = heatmap.annotate_heatmap(im, valfmt="{x:.1f}")

ax.set_xlabel('relationship')
ax.set_ylabel('hours_per_week')

fig.tight_layout()
plt.show()#Quem trabalha mais horas em média: o marido, a esposa, pessoas com filhos, etc? Este comportamento varia dependendo da idade?

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
import numpy as np
import heatmap

atributos = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',  'relationship', 'race', 'sex', 'capital_gain',  'capital-loss', 'hours_per_week', 'native-country', 'class_']

adult = pd.read_csv('adult.data', names = atributos, delimiter = ',')

rel = adult[['relationship', 'hours_per_week', 'age']]

s_hours_per_week = adult['hours_per_week']
s_age = adult['age']
s_relationship = adult['relationship']

rel = pd.concat([s_hours_per_week, s_age, s_relationship], axis=1)

rel = rel.sort_values(['relationship', 'hours_per_week', 'age']).astype(str)

for i in range(0, 100, 10):
	for j in range(i+1, (i + 11), 1):
		rel['hours_per_week'].replace(str(j), str(i+1) + '-' + str(i+10), inplace = True)

relationship = preprocessing.LabelEncoder()
relationship.fit(rel['relationship'])
rel['relationship'] = relationship.transform(rel['relationship'])
#['Husband' 'Not-in-family' 'Other-relative' 'Own-child' 'Unmarried' 'Wife']

hours_per_week = preprocessing.LabelEncoder()
hours_per_week.fit(rel['hours_per_week'])
rel['hours_per_week'] = hours_per_week.transform(rel['hours_per_week'])
#['1-10' '11-20' '21-30' '31-40' '41-50' '51-60' '61-70' '71-80' '81-90' '91-100']

'''age = preprocessing.LabelEncoder()
age.fit(rel['age'])
rel['age'] = age.transform(rel['age'])
#['11-20' '21-30' '31-40' '41-50' '51-60' '61-70' '71-80' '81-90']'''

rel = rel.sort_values(['relationship', 'hours_per_week', 'age'])

#rel.drop_duplicates(inplace=True)

#criacao de matriz
vetor1 = rel['hours_per_week'].values
vetor2 = rel['relationship'].values
valores = rel['age'].values

m = len(set(vetor1))
n = len(set(vetor2))

matriz = []

for i in range(0, m, 1):
	aux = []
	for j in range(0, n, 1):
		aux.append(0)
	matriz.append(aux)

for i in range(0, len(valores), 1):
	matriz[vetor1[i]][vetor2[i]] = rel.query('hours_per_week == "' + str(vetor1[i]) + '" & relationship == "' + str(vetor2[i]) + '"')['age'].astype(int).mean()

fig, ax = plt.subplots()

im, cbar = heatmap.heatmap(np.array(matriz), hours_per_week.inverse_transform(np.arange(m)), relationship.inverse_transform(np.arange(n)), ax=ax, cmap="YlGn", cbarlabel="average age")
texts = heatmap.annotate_heatmap(im, valfmt="{x:.1f}")

ax.set_xlabel('relationship')
ax.set_ylabel('hours_per_week')
plt.subplots_adjust(left=0.10, bottom=0.20, right=0.67, top=0.99, wspace=0.20, hspace=0.20)
fig.tight_layout()
plt.show()
