# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:47:39 2020

@author: Saad
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


bankdata2 = pd.read_csv("trainingCommonVoicePreProcessedWithAgeGroupsRemovingOther.csv")

X = bankdata2.iloc[:, :-4].values
y = bankdata2.iloc[:, [34,36,37]].values



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

    
# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train[:,0])

# Predicting the Test set results
y_pred = classifier.predict(X_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test[:,0], y_pred)

from sklearn.metrics import accuracy_score, classification_report
print(cm)
print(classification_report(y_test[:,0],y_pred))
print("accuracy:",accuracy_score(y_test[:,0],y_pred,normalize=True))

