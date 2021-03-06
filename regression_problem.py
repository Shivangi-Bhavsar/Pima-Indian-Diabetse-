# -*- coding: utf-8 -*-
"""Regression Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QEqYyBW-Qwq_V8_PS31I94i1k1oYPG_T
"""

I am a real estate agent and I have 3 clients selling their homes.  I’m having trouble working 
with them and I need your data science skills.  They don’t trust Zillow or any online service for 
setting prices.  They’ve been burned by other real estate agents and the pricing formulas used.   
 
These homes are in the Boston Area and a trusted advisor told me that you may be able to use 
the boston housing dataset to help answer these questions: 
 
§ What price would you recommend for each client? 
§ Do these prices seem appropriate?  How do you know? 
§ What other factors should we be considering

import numpy as np
import pandas as pd
import matplotlib as mp
from matplotlib import pyplot as plt
import seaborn as sns   
from sklearn.model_selection import train_test_split

"""Variables in order:
 CRIM     per capita crime rate by tow


 ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
 INDUS    proportion of non-retail business acres per town
 CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
 NOX      nitric oxides concentration (parts per 10 million)
 RM       average number of rooms per dwelling
 AGE      proportion of owner-occupied units built prior to 1940
 DIS      weighted distances to five Boston employment centres
 RAD      index of accessibility to radial highways
 TAX      full-value property-tax rate per $10,000
 PTRATIO  pupil-teacher ratio by town
 B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
 LSTAT    % lower status of the population
 MEDV     Median value of owner-occupied homes in $1000's
"""

df=pd.read_csv("/Boston.csv")
df.head()

print ("Boston housing dataset has {} data points with {} variables each.".format(*df.shape))

df.describe() #checking

df.isnull().values.any()

correlation = df.corr(method='pearson')
correlation

price = df['medv']
col=['rm','lstat','ptratio']
feature_predictors= df[col]

for var in feature_predictors:
    sns.regplot(df[var],price)
    plt.show()

#splitting data to predict the housing price

price_train, price_test, feature_predictors_train, feature_predictors_test = train_test_split(price, feature_predictors, test_size=0.3, random_state=3)

#applying linear regression model

from sklearn.linear_model import LinearRegression

model= LinearRegression()

model.fit(feature_predictors_train,price_train)

model.fit(feature_predictors_test,price_test)

print("Accuraccy:",model.score(feature_predictors_train,price_train)*100)

print("Accuraccy:",model.score(feature_predictors_train,price_train)*100)

price_predicted = model.predict(feature_predictors_test)
price_predicted

client_data=[[5,19,20],[9,8,10],[4,37,10]]

for i, price in enumerate(model.predict(client_data)):
  print ("Predicted selling price for Client {}'s home: ${:,.2f}".format(i+1, price))

feature1_predictors= df.iloc[:,0:13]

price1=df.medv

price1_train, price1_test, feature1_predictors_train, feature1_predictors_test = train_test_split(price1, feature1_predictors, test_size=0.3, random_state=3)

#applying linear regression model

from sklearn.linear_model import LinearRegression

model= LinearRegression()

model.fit(feature1_predictors_train,price1_train)

model.fit(feature1_predictors_test,price1_test)

print("Accuraccy:",model.score(feature1_predictors_train,price1_train)*100)

print("Accuraccy:",model.score(feature1_predictors_train,price1_train)*100)

for var in feature1_predictors:
    sns.regplot(df[var],price)
    plt.show()