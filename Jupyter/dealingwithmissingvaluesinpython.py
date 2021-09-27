# -*- coding: utf-8 -*-
"""DealingWithMissingValuesInPython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-hcg3DyqefNvgo7l4F2b-fmtoE3DPbIO
"""

#Here we are going to use PIMA Indian Daibities Dataset
#The variable names are as follows:
Pregnancies – Number of times pregnant
Glucose – Plasma glucose concentration a 2 hours in an oral glucose tolerance test
Blood Pressure – Diastolic blood pressure (mm Hg)
Skin Thickness – Triceps skinfold thickness (mm)
Insulin – 2-Hour serum insulin (mu U/ml)
BMI – Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction – Diabetes pedigree function
Age – Age in years
Outcome – Class variable (0 or 1)

#Importing necessary modules
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# importing the dataset
from google.colab import files
uploaded = files.upload()

import io
data = pd.read_csv(io.BytesIO(uploaded['diabetes.csv']))
# Dataset is now stored in a Pandas Dataframe

#Checking the shape of our data
data.shape

#Printing top 5 rows to make us familier with dataset
data.head()

#Using .info() function on a DataFrame we can get basic information about our DataFrame like features and their datatypes, no of missing values, number of rows or columns etc. as shown below:
data.info()

#Checking basic test statistics like mean, median etc.
data.describe()

#let’s check how much data our in dataset is missing (in form of 0):
(data.iloc[:,1:6] == 0).sum()

#Let's convert the 0’s into NaN by using .replace() method
for i in range(1,6):
    data.iloc[:, i].replace(0, np.nan, inplace=True)

#Again checking how much data in our dataset is mentioned as 0:
(data.iloc[:,1:6] == 0).sum()

#let’s again for confirmation, check our dataset using .head() method and print the top 10 rows
data.head(10)

#The above process is not generally advised because it will delete all observations where any of variables is missing ultimately reducing the size of our dataset and quality of our model.
data = data.dropna()

#Checking how much data is left after using .dropna() method
data.shape

#Almost 50% of our data is deleted which is not good for us. 
#If only a few rows contain missing values, then it’s not so bad, but generally, we need a more robust method. 
#So this method is only advised to use if NaN values are few in numbers.

#Filling missing values with a test statistics like mean, median or mode.
#Showing here with mean only

mean_value=data['Age'].mean()
data['Age']=data['Age'].fillna(mean_value)

#Using Forward fill and Backward fill
#Backward fill
data.fillna(method='bfill')
#Forward Fill
data.fillna(method='ffill')

#Using imputer and fitting out the model at once by using a Sklearn’s pipeline object as shown below:
import sklearn.linear_model as sk
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values='NaN', strategy='mean')
imp = imp
log = sk.LogisticRegressionCV()
steps = [('imputation', imp), ('logistic_regresson', log)]
pipeline = Pipeline(steps)

print(data)