import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
from lightgbm import LGBMClassifier
from matplotlib import pyplot
from sklearn.metrics import accuracy_score, roc_auc_score
import shap
from sklearn.feature_selection import RFECV

"""
Допустим, что источник данных находится на папке с известных сервером
В данном скрипте данные загружаются 

"""

df_train = pd.read_csv(r'C:\Users\user\Desktop\HCB\application_train.csv')
df_test = pd.read_csv(r'C:\Users\user\Desktop\HCB\application_test.csv')

