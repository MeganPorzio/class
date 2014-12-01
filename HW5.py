# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 21:29:39 2014

@author: Student
"""

import pandas
import matplotlib.pyplot as plt

wine = pandas.read_csv("wine.data", header=None)
wine.columns = ['Class','Alcohol','Malic Acid','Ash','Alcalinity of Ash','Magnesium','Total Phenols','Flavanoids','Nonflavanoid Phenols','Proanthocyanins','Color Intensity','Hue','OD280/OD315 of Diluted Wines','Proline']

print wine

wine.hist([1])