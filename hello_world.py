# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 10:26:58 2018

@author: RAMA
"""

import pandas as pd
from sklearn import tree
import os

titanic_train =pd.read_csv("C:\\Users\\RAMA\\Downloads\\titanic\\train.csv")
 titanic_train.shape
 titanic_train.info()
 
 X_titanic_train = titanic_train[['Pclass','SibSp','Parch']]
 Y_titanic_train = titanic_train['Survived']
 
 dt = tree.DecisionTreeClassifier()
 dt.fit(X_titanic_train,Y_titanic_train)
 
 titanic_test =pd.read_csv('C:\\Users\\RAMA\\Downloads\\titanic\\test.csv')
 X_test = titanic_test[['Pclass','SibSp','Parch']]
 
 os.getcwd()
 
 titanic_test['Survived']=dt.predict(X_test)
 titanic_test.to_csv("submission_titanic.csv",columns=['Passenger Id',"Survived"],index=False)
 
 
 titanic_train1=pd.get_dummies(titanic_train,columns=['Pclass','Sex','Embarked'])
 titanic_train1.shape
 