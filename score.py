from sklearn.metrics import accuracy_score, roc_auc_score
import shap
from sklearn.feature_selection import RFECV


def accuracy_score(predict, target):
    metrics = roc_auc_score(target, predict)
    print('LightGBM: ROC AUC=%.3f' % (metrics))