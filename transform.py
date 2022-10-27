import numpy as np
from lightgbm import LGBMClassifier


import extract ##загружаем данные???

target = df_train['TARGET']
train = df_train.drop(labels= ['TARGET'], axis = 1)

cat = ['NAME_CONTRACT_TYPE',
       'CODE_GENDER',
       'FLAG_OWN_CAR',
       'FLAG_OWN_REALTY',
       'NAME_TYPE_SUITE',
       'NAME_INCOME_TYPE',
       'NAME_EDUCATION_TYPE',
       'NAME_FAMILY_STATUS',
       'NAME_HOUSING_TYPE',
       'OCCUPATION_TYPE',
       'WEEKDAY_APPR_PROCESS_START',
       'ORGANIZATION_TYPE',
       'FONDKAPREMONT_MODE',
       'HOUSETYPE_MODE',
       'WALLSMATERIAL_MODE',
       'EMERGENCYSTATE_MODE'] #делаем глобальную переменную, так как используется в двух функциях

    def transform_cat_feature(date_train, date_test, date_bureau):
    """
    :param date_train: ## тут что писать?
    :param date_test:
    :return:
    """
        for c in cat:
            date_train[c] = date_train[c].astype('category')
        for c in cat:
            date_test[c] = date_test[c].astype('category')

        cat_b = ['CREDIT_ACTIVE', 'CREDIT_CURRENCY', 'CREDIT_TYPE']
        for c in cat_b:
            date_bureau[c] = date_bureau[c].astype('category')

        return date_train, date_test, date_bureau

    def new_feature(train_f, test_f, bureau_f):
        #новые фичи по трейн и тест
        #трайн
        train_f['CREDIT_PERCENT'] = train_f['AMT_ANNUITY'] / train_f['AMT_CREDIT']
        train_f['ANNUITY_INCOME'] = train_f['AMT_ANNUITY'] / train_f['AMT_INCOME_TOTAL']
        train_f['CREDIT_INCOME'] = train_f['AMT_CREDIT'] / train_f['AMT_INCOME_TOTAL']
        train_f['BIRTH_EMPLOYED'] = train_f['DAYS_EMPLOYED'] / train_f['DAYS_BIRTH']
        train_f['CHILDREN_CNT_INCOME_PERCENT'] = train_f['AMT_INCOME_TOTAL'] / train_f['CNT_CHILDREN']

        #тест
        test_f['CREDIT_PERCENT'] = test_f['AMT_ANNUITY'] / test_f['AMT_CREDIT']
        test_f['ANNUITY_INCOME'] = test_f['AMT_ANNUITY'] / test_f['AMT_INCOME_TOTAL']
        test_f['CREDIT_INCOME'] = test_f['AMT_CREDIT'] / test_f['AMT_INCOME_TOTAL']
        test_f['BIRTH_EMPLOYED'] = test_f['DAYS_EMPLOYED'] / test_f['DAYS_BIRTH']
        test_f['CHILDREN_CNT_INCOME_PERCENT'] = test_f['AMT_INCOME_TOTAL'] / test_f['CNT_CHILDREN']

        #новые фичи по бюро
        bureau_f['CREDIT_DURATION'] = -bureau_f['DAYS_CREDIT'] + bureau_f['DAYS_CREDIT_ENDDATE']
        bureau_f['ENDDATE_DIFF'] = bureau_f['DAYS_CREDIT_ENDDATE'] - bureau_f['DAYS_ENDDATE_FACT']
        bureau_f['DEBT_rate'] = bureau_f['AMT_ANNUITY'] / bureau_f['AMT_CREDIT_SUM_DEBT']
        bureau_f['DEBT_over'] = bureau_f['AMT_CREDIT_SUM_OVERDUE'] / bureau_f['AMT_CREDIT_SUM_DEBT']
        bureau_f['current_rate_debt'] = bureau_f['AMT_CREDIT_SUM'] / bureau_f['AMT_CREDIT_SUM_DEBT']
        bureau_f['DEBT_PERCENTAGE'] = bureau_f['AMT_CREDIT_SUM_LIMIT'] / bureau_f['AMT_CREDIT_SUM_DEBT']
        bureau_f['CNT_sum_CREDIT_PROLONG'] = bureau_f['AMT_CREDIT_SUM_DEBT'] / bureau_f['CNT_CREDIT_PROLONG']
        bureau_f_n = bureau_f.groupby('SK_ID_CURR')['AMT_CREDIT_SUM'].agg(['max','mean','min'])

        return train_f, test_f, bureau_f_n
