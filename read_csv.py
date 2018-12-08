# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 18:02:47 2018

@author: RAMA
"""

import pandas as pd

print(pd.__version__)

data_frame = pd.read_csv('C:\\Users\\RAMA\\Downloads\\titanic\\train.csv')

print(data_frame.shape)

print(data_frame.info())

print(data_frame.describe())

data_frame['Fare']

data_frame.head(6)

data_frame.tail(6)

data_frame.iloc[10:20]

data_frame.loc[10:20,['Name','Age']]

data_frame.loc[data_frame.Sex=='female','Sex']

data_frame.loc[data_frame.Sex=='female','Age']

data_frame.groupby(["Embarked"]).size()

data_frame.groupby(["Pclass",'Sex']).size()

data_frame.groupby(["Pclass",'Embarked','Sex']).size()

data_frame.groupby(["Embarked",'Pclass']).mean()

data_frame.groupby(["Embarked",'Pclass']).mean()['Fare']

