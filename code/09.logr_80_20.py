# -*- coding: utf-8 -*-
"""04.machine_learning_tasks_oneImg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QMSIfeVeILTT-F9iwzLalJmYrsUmOFd2

# Author: [Yunting Chiu](https://www.linkedin.com/in/yuntingchiu/)
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
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
#from sklearn.metrics import roc_curve
#from sklearn.metrics import roc_auc_score


# Exploratory Data Analysis
##Read the data (`.npz` file)

data_zipped = np.load("np_data_all.npz", allow_pickle=True)

for item in data_zipped.files:
    print(item)
    print(data_zipped[item])
    
#print(data_zipped[item].shape)
data = data_zipped[item]

"""## Check the length of $X$ and $y$"""

X = []
y = []
for i in data:
  X.append(i[0])
  y.append(i[1])
#print(len(X))
#print(len(y))
print("The length of X feature is", len(X[1]))
print("The length should be " + str((6984+7000)))
print("data dimension:",data.shape)

"""## Visualization"""

fake_cnt = 0
real_cnt = 0
for i in data:
  if i[1] == "fake":
    fake_cnt += 1
  else:
    real_cnt += 1

#print(fake_cnt)
#print(real_cnt)
df = [['fake', fake_cnt], ['real', real_cnt]]
df = pd.DataFrame(df, columns=['image_type', 'count'])
#ax = df.plot.bar(x='video_type', y='count', rot=0)
fig = plt.figure()
plt.bar(df['image_type'], df['count'])
plt.xlabel("Image Type")
plt.ylabel("Count")
plt.savefig('09.count_type.png')

"""# Machine Learning Task

"""



"""## Support Vector Machine"""

start_time = time.time()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) # 80% for training, 20 for of testing
logr_clf = LogisticRegression(random_state=42, C=1)
logr_clf.fit(X_train, y_train)
y_pred = logr_clf.predict(X_test)

print("--- %s seconds ---" % (time.time() - start_time))
print("----------Confusion Matrix----------------")
print(confusion_matrix(y_test, y_pred))

### SVM Confusion Matrix

#plot_confusion_matrix(svm_clf, X_test, y_test, values_format = '.0f') 
#plt.figure(figsize=(12,8))
#plt.show()
conf_matrix = confusion_matrix(y_true = y_test, y_pred = y_pred)
# Print the confusion matrix using Matplotlib

fig, ax = plt.subplots(figsize=(7.5, 7.5))
ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(x=j, y=i,s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()
plt.savefig('09.confusion_matrix.png')


### SVM Accuracy Score

print("----------Accuracy Score----------------")
print(accuracy_score(y_test, y_pred))

print("------------Classification Report----------")
target_names = ['fake', 'real']
print(classification_report(y_test, y_pred, target_names=target_names))