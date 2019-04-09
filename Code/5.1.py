#O que mais você consegue explorar nesta base? Apresente pelo menos mais uma relação que conseguir encontrar utilizando uma técnica de visualização.

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
import numpy as np

atributos = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation',  'relationship', 'race', 'sex', 'capital_gain',  'capital-loss', 'hours_per_week', 'native_country', 'class_']

adult = pd.read_csv('adult.data', names=atributos, delimiter=',')

workclass = preprocessing.LabelEncoder()
education = preprocessing.LabelEncoder()
marital_status = preprocessing.LabelEncoder()
occupation = preprocessing.LabelEncoder()
relationship = preprocessing.LabelEncoder()
race = preprocessing.LabelEncoder()
sex = preprocessing.LabelEncoder()
native_country = preprocessing.LabelEncoder()
class_ = preprocessing.LabelEncoder()

adult['workclass'] = workclass.fit_transform(adult['workclass'])
#['?' 'Federal-gov' 'Local-gov' 'Never-worked' 'Private' 'Self-emp-inc' 'Self-emp-not-inc' 'State-gov' 'Without-pay']
adult['education'] = education.fit_transform(adult['education'])
#['10th' '11th' '12th' '1st-4th' '5th-6th' '7th-8th' '9th' 'Assoc-acdm' 'Assoc-voc' 'Bachelors' 'Doctorate' 'HS-grad' 'Masters' 'Preschool' 'Prof-school' 'Some-college']
adult['marital_status'] = marital_status.fit_transform(adult['marital_status'])
#['Divorced' 'Married-AF-spouse' 'Married-civ-spouse' 'Married-spouse-absent' 'Never-married' 'Separated' 'Widowed']
adult['occupation'] = occupation.fit_transform(adult['occupation'])
#['?' 'Adm-clerical' 'Armed-Forces' 'Craft-repair' 'Exec-managerial' 'Farming-fishing' 'Handlers-cleaners' 'Machine-op-inspct' 'Other-service' 'Priv-house-serv' 'Prof-specialty' 'Protective-serv' 'Sales' 'Tech-support' 'Transport-moving']
adult['relationship'] = relationship.fit_transform(adult['relationship'])
#['Husband' 'Not-in-family' 'Other-relative' 'Own-child' 'Unmarried' 'Wife']
adult['race'] = race.fit_transform(adult['race'])
#['Amer-Indian-Eskimo' 'Asian-Pac-Islander' 'Black' 'Other' 'White']
adult['sex'] = sex.fit_transform(adult['sex'])
#['Female' 'Male']
adult['native_country'] = native_country.fit_transform(adult['native_country'])
#['?' 'Cambodia' 'Canada' 'China' 'Columbia' 'Cuba' 'Dominican-Republic' 'Ecuador' 'El-Salvador' 'England' 'France' 'Germany' 'Greece' 'Guatemala' 'Haiti' 'Holand-Netherlands' 'Honduras' 'Hong' 'Hungary' 'India' 'Iran' 'Ireland' 'Italy' 'Jamaica' 'Japan' 'Laos' 'Mexico' 'Nicaragua' 'Outlying-US(Guam-USVI-etc)' 'Peru' 'Philippines' 'Poland' 'Portugal' 'Puerto-Rico' 'Scotland' 'South' 'Taiwan' 'Thailand' 'Trinadad&Tobago' 'United-States' 'Vietnam' 'Yugoslavia']
adult['class_'] = class_.fit_transform(adult['class_'])
#['<=50K' '>50K']

corr = adult.corr()

fig, ax = plt.subplots()

plt.imshow(corr, cmap='hot', interpolation='none')  
plt.colorbar()  
plt.xticks(range(len(corr)), corr.columns, rotation = 'vertical')  
plt.yticks(range(len(corr)), corr.columns)
plt.subplots_adjust(left=0.10, bottom=0.20, right=0.80, top=0.99, wspace=0.20, hspace=0.20)


plt.show()
