# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 21:29:39 2014

@author: Student
"""

import pandas
import numpy as np
from sklearn import cross_validation


wine = pandas.read_csv("wine.data", header=None)
wine.columns = ['Class','Alcohol','Malic Acid','Ash','Alcalinity of Ash','Magnesium','Total Phenols','Flavanoids','Nonflavanoid Phenols','Proanthocyanins','Color Intensity','Hue','OD280/OD315 of Diluted Wines','Proline']

wine.hist([1])

data_values=wine.values
all_array=np.array(data_values)
data_array=all_array[:,1:]
label_array=all_array[:,0:1]
label_array=label_array.ravel()


data_train, data_test, label_train, label_test = cross_validation.train_test_split(data_array,label_array)