from sklearn.metrics import accuracy_score, roc_auc_score
import shap
from sklearn.feature_selection import RFECV


def accuracy_score(predict, target):
    metrics = roc_auc_score(target, predict)
    print('LightGBM: ROC AUC=%.3f' % (metrics))

def shap_ml(model, train, test):
    shap_1 = shap.TreeExplainer(model).shap_values(train)
    shap.summary_plot(shap_1, test,
                  max_display=25, auto_size_plot=True)