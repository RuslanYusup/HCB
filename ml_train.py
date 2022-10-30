import pandas as pd
import numpy as np #если не выделяет - значит не используется в скрипте?
from lightgbm import LGBMClassifier


"""
1. Окончательно готовим данные для модели
2. Отправляем в модель

"""

def prepare_data_model(train, test, buro): #обязательно ли прописывать также как в main?
    bureau_f = buro.groupby('SK_ID_CURR')['AMT_CREDIT_SUM'].agg(['max','mean','min'])

    train_n = train.merge(right=bureau_f.reset_index(), how='left', on='SK_ID_CURR')
    test_n = test.merge(right=bureau_f.reset_index(), how='left', on='SK_ID_CURR')
    train_b, test_b = train_n.align(test_n, join='inner', axis=1)

    return train_b, test_b

def model_fit(train_b, test_b, target):
    model = LGBMClassifier(objective="binary")
    model.fit(train_b, target, categorical_feature=cat)
    predict = model.predict_proba(test_b)[:, 1]

    return predict

