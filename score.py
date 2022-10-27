from sklearn.metrics import accuracy_score, roc_auc_score
import transform

train = train_f.merge(right=bureau_f_n.reset_index(), how='left', on='SK_ID_CURR')
test = test_f.merge(right=bureau_f_n.reset_index(), how='left', on='SK_ID_CURR')
train, test = train_f.align(train_f, join='inner', axis=1)



def accuracy_score(train, target, test):
    model = LGBMClassifier(objective="binary")
    model.fit(train, target, categorical_feature=cat)
    predict = model.predict_proba(test)[:, 1]
    metrics = roc_auc_score(target, predict)
    print('LightGBM: ROC AUC=%.3f' % (metrics))