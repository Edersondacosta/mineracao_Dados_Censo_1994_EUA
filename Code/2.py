#Investigue a relação entre ganho de capital e ganho anual: qual é o ganho médio de capital de acordo com o ganho anual? Observe também o histograma do ganho de capital. O que podemos inferir sobre essas observações?

import pandas as pd
import matplotlib.pyplot as plt

atributos = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',  'relationship', 'race', 'sex', 'capital_gain',  'capital-loss', 'hours-per-week', 'native-country', 'class_']

adult = pd.read_csv('adult.data', names = atributos, delimiter = ',')

rel = adult[['capital_gain', 'class_']]

menor_igual = rel.query('class_ == "<=50K" & capital_gain != 0')['capital_gain']
maior = rel.query('class_ == ">50K" & capital_gain != 0')['capital_gain']

bins = 10

fig, axs = plt.subplots(1, 2)
axs[0].hist(menor_igual, bins = bins)
axs[1].hist(maior, bins = bins)

plt.subplots_adjust(left=0.05, bottom=0.05, right=0.99, top=0.99, wspace=0.20, hspace=0.20)
axs[0].yaxis.grid(True)
axs[1].yaxis.grid(True)
axs[0].set_xlabel('<=50K')
axs[1].set_xlabel('>50K')
axs[0].set_ylabel('Frequencia')
axs[1].set_ylabel('Frequencia')

plt.show()
