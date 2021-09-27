# -*- coding: utf-8 -*-
"""Linear Regression in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dXbHQZJxdRNntJLS-YsunCJ6mHALoTJa
"""

Linear Regression:
- Simple Linear Regression: Simple linear regression is an approach for predicting a response using a single feature.
It is assumed that the two variables are linearly related. 
Hence, we try to find a linear function that predicts the response value(y) as accurately as possible as a function of the feature or independent variable(x).

- Multiple Linear Regression: Multiple linear regression attempts to model the relationship between two or more features and a response by fitting a linear equation to the observed data.

Equation of Simple Linear Regression, where bo is the intercept, b1 is coefficient or slope, x is the independent variable and y is the dependent variable.
=>  y = b0 + b1x

Equation of Multiple Linear Regression, where bo is the intercept, b1,b2,b3,b4…,bn are coefficients or slopes of the independent variables x1,x2,x3,x4…,xn and y is the dependent variable.
=>  y = b0 + b1x1 + b2x2 + b3x3 + ..... + bnxn

A Linear Regression model’s main aim is to find the best fit linear line and the optimal values of intercept and coefficients such that the error is minimized.
Error is the difference between the actual value and Predicted value and the goal is to reduce this difference.

# importing the dataset
from google.colab import files
uploaded = files.upload()

import io

# Commented out IPython magic to ensure Python compatibility.
# importing libraries
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading data 
housing = pd.read_csv('housing.csv')
print(housing.shape)
housing.head()

housing.info()

housing['ocean_proximity'].value_counts()

housing.describe()

housing.hist(bins=50, figsize=(20, 15))
plt.show()

# median income looks like an imp feature

housing['median_income'].hist()

housing_refine = housing.drop('ocean_proximity', axis = 1)

housing_refine.info()

housing_refine = housing_refine.dropna(axis = 0)
housing_refine.info()

X = housing_refine.drop('median_house_value', axis = 1)
y = housing_refine['median_house_value']

X.info()

print(y.shape)

plt.scatter(X['total_bedrooms'], y)
plt.xlabel('total_bedrooms')
plt.ylabel('House Price')

X.head()

color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
X['total_bedrooms'].plot.box(color=color)

import sklearn as sk
import sklearn.linear_model as slm
from sklearn.model_selection import train_test_split

LR = slm.LinearRegression()
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.25)
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

LR.fit(X_train, Y_train)

predict = LR.predict(X_test)

print('Predicted Value :',predict[0])
print('Actual Value :',Y_test.values[0])

LR.score (X_test, Y_test)

gr = pd.DataFrame({'Predicted':predict,'Actual':Y_test})
gr = gr.reset_index()
gr = gr.drop(['index'],axis=1)
plt.plot(gr[:1000])
plt.legend(['Actual','Predicted'])
#gr.plot.bar();