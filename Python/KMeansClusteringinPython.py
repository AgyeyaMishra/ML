# -*- coding: utf-8 -*-
"""K-Means Clustering in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Ps1qSSZUPupsbs2y3S8G2wVDkCDfI9r

## K-Means Clustering on Iris Dataset

#### Author - Agyeya Mishra
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sklearn.metrics as sm
# %matplotlib inline

iris = datasets.load_iris()
print(iris.data)

print(iris.target_names)

print(iris.target)

x = pd.DataFrame(iris.data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
y = pd.DataFrame(iris.target, columns=['Target'])

x.head()

y.head()

plt.figure(figsize=(12,3))
colors = np.array(['red', 'green', 'blue'])
iris_targets_legend = np.array(iris.target_names)
red_patch = mpatches.Patch(color='red', label='Setosa')
green_patch = mpatches.Patch(color='green', label='Versicolor')
blue_patch = mpatches.Patch(color='blue', label='Virginica')


plt.subplot(1, 2, 1)
plt.scatter(x['Sepal Length'], x['Sepal Width'], c=colors[y['Target']])
plt.title('Sepal Length vs Sepal Width')
plt.legend(handles=[red_patch, green_patch, blue_patch])

plt.subplot(1,2,2)
plt.scatter(x['Petal Length'], x['Petal Width'], c= colors[y['Target']])
plt.title('Petal Length vs Petal Width')
plt.legend(handles=[red_patch, green_patch, blue_patch])

iris_k_mean_model = KMeans(n_clusters=3)
iris_k_mean_model.fit(x)

print(iris_k_mean_model.labels_)

print (iris_k_mean_model.cluster_centers_)

plt.figure(figsize=(12,3))

colors = np.array(['red', 'green', 'blue'])

predictedY = np.choose(iris_k_mean_model.labels_, [1, 0, 2]).astype(np.int64)

plt.subplot(1, 2, 1)
plt.scatter(x['Petal Length'], x['Petal Width'], c=colors[y['Target']])
plt.title('Before classification')
plt.legend(handles=[red_patch, green_patch, blue_patch])

plt.subplot(1, 2, 2)
plt.scatter(x['Petal Length'], x['Petal Width'], c=colors[predictedY])
plt.title("Model's classification")
plt.legend(handles=[red_patch, green_patch, blue_patch])

sm.accuracy_score(predictedY, y['Target'])

"""### Interpretation of Confusion Matrix
Correctly identifed all 0 classes as 0’s correctly classified 48 class 1’s but miss-classified 2 class 1’s as class 2 correctly classified 36 class 2’s but miss-classified 14 class 2’s as class 1
"""

sm.confusion_matrix(predictedY, y['Target'])
