import pandas as pd
import numpy as np

import configparser




"""
1. Алгоритм Lightgbm просит изменить тип категоривальных переменных, поэтому
для дата сетов train, test и buro мы будем приводит их в соответствие 

2. Выделим целевой таргет в отдельный сет
"""

def transform_cat_feature(date_train, date_test, date_bureau):
"""
:param date_train: сырой датафрейм трейн
:param date_test:  сырой датафрейм тест
:return: датафреймы, трейн и тест с приведенным типом данных
"""
    config = configparser.ConfigParser()
    config.read('cat.ini') # пишут, что выдает только строки, не уверен что будет работать...

    for c in cat:
        train[c] = date_train[c].astype('category')
        test[c] = date_test[c].astype('category')

    for c in cat_b:
        bureau[c] = date_bureau[c].astype('category')

    return date_train, date_test, date_bureau


def create_train(date_train):
    target = date_train['TARGET']
    train = date_train.drop(labels= ['TARGET'], axis = 1)

    return target, train
