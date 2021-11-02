# -*- coding: utf-8 -*-
"""04.machine_learning_tasks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QMSIfeVeILTT-F9iwzLalJmYrsUmOFd2
"""
# Author: Yunting Chiu

import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
import os
os.system('pip install --upgrade scikit-learn')

# Commented out IPython magic to ensure Python compatibility.
#wd
# %cd /content/drive/MyDrive/American_University/2021_Fall/DATA-793-001_Data Science Practicum/data
#!pwd

"""# Exploratory Data Analysis
##Read the data (npz file)
"""

data_zipped = np.load("np_data_all.npz", allow_pickle=True)

for item in data_zipped.files:
    print(item)
    print(data_zipped[item])
    
print(data_zipped[item].shape)

data = data_zipped[item]

"""## Check the length of $X$ and $y$"""

X = []
y = []
for i in data:
  X.append(i[0])
  y.append(i[1])
print(len(X))
print(len(y))
print("The length should be " + str((6984+7000)))

#print(X)
#print(y)

"""## Visualization

# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

# Machine Learning Task
"""

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler # standardize features by removing the mean and scaling to unit variance.
from sklearn.metrics import confusion_matrix
#from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

"""## Support Vector Machine"""

start_time = time.time()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) # 80% for training, 20 for of testing
svm_clf = make_pipeline(StandardScaler(), SVC(gamma='scale', C = 1)) # clf = classifer
svm_clf.fit(X_train, y_train)
y_pred = svm_clf.predict(X_test)

print("--- %s seconds ---" % (time.time() - start_time))
print(confusion_matrix(y_test, y_pred))

"""### SVM Confusion Matrix


"""

#plot_confusion_matrix(svm_clf, X_test, y_test, values_format = '.0f') 
#plt.figure(figsize=(12,8))
#plt.show()

"""### SVM Accuracy Score"""

print(accuracy_score(y_test, y_pred))

target_names = ['fake', 'real']
print(classification_report(y_test, y_pred, target_names=target_names))

"""## Random Forest Classifier"""

start_time = time.time()
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) # 80% for training, 20 for of testing
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42, bootstrap=True)
rf_clf.fit(X_train, y_train)
y_pred = rf_clf.predict(X_test)

print("--- %s seconds ---" % (time.time() - start_time))
print(confusion_matrix(y_test, y_pred))

"""### Random Forest Accuracy Score"""

print(accuracy_score(y_test, y_pred))

"""## Logistic Regression"""

#start_time = time.time()
#lg_clf = LogisticRegression(random_state=42, C=1)
#lg_clf.fit(X_train, y_train)
#y_pred = lg_clf.predict(X_test)

#print("--- %s seconds ---" % (time.time() - start_time))
#print(confusion_matrix(y_test, y_pred))

"""### Logistic Regression Accuracy Score"""

#print(accuracy_score(y_test, y_pred))


"""# References
- https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ch05.html#idm45022165153592
- https://github.com/scikit-learn/scikit-learn/issues/16127
- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
"""