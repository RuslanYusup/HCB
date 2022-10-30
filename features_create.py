import pandas as pd
import numpy as np

"""
Создаем новые фичи для датасетов
"""

def new_feature(train, df_test, buro):
    #новые фичи по трейн и тест
    #трайн

    train['CREDIT_PERCENT'] = train['AMT_ANNUITY'] / train['AMT_CREDIT']
    train['ANNUITY_INCOME'] = train['AMT_ANNUITY'] / train['AMT_INCOME_TOTAL']
    train['CREDIT_INCOME'] = train['AMT_CREDIT'] / train['AMT_INCOME_TOTAL']
    train['BIRTH_EMPLOYED'] = train['DAYS_EMPLOYED'] / train['DAYS_BIRTH']
    train['CHILDREN_CNT_INCOME_PERCENT'] = train['AMT_INCOME_TOTAL'] / train['CNT_CHILDREN']

    #тест
    df_test['CREDIT_PERCENT'] = df_test['AMT_ANNUITY'] / df_test['AMT_CREDIT']
    df_test['ANNUITY_INCOME'] = df_test['AMT_ANNUITY'] / df_test['AMT_INCOME_TOTAL']
    df_test['CREDIT_INCOME'] = df_test['AMT_CREDIT'] / df_test['AMT_INCOME_TOTAL']
    df_test['BIRTH_EMPLOYED'] = df_test['DAYS_EMPLOYED'] / df_test['DAYS_BIRTH']
    df_test['CHILDREN_CNT_INCOME_PERCENT'] = df_test['AMT_INCOME_TOTAL'] / df_test['CNT_CHILDREN']

    #новые фичи по бюро
    buro['CREDIT_DURATION'] = -buro['DAYS_CREDIT'] + buro['DAYS_CREDIT_ENDDATE']
    buro['ENDDATE_DIFF'] = buro['DAYS_CREDIT_ENDDATE'] - buro['DAYS_ENDDATE_FACT']
    buro['DEBT_rate'] = buro['AMT_ANNUITY'] / buro['AMT_CREDIT_SUM_DEBT']
    buro['DEBT_over'] = buro['AMT_CREDIT_SUM_OVERDUE'] / buro['AMT_CREDIT_SUM_DEBT']
    buro['current_rate_debt'] = buro['AMT_CREDIT_SUM'] / buro['AMT_CREDIT_SUM_DEBT']
    buro['DEBT_PERCENTAGE'] = buro['AMT_CREDIT_SUM_LIMIT'] / buro['AMT_CREDIT_SUM_DEBT']
    buro['CNT_sum_CREDIT_PROLONG'] = buro['AMT_CREDIT_SUM_DEBT'] / buro['CNT_CREDIT_PROLONG']

    return train, df_test, buro