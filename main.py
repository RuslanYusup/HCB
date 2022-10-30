import extract
import transform
import features_create
import ml_train
import score


"""
Main script mor implementing ETL process
1. extract - download all date to main directory
2. transform - prepare date to Lightgbm
3. features_create - create new features for model
4. Ml_train - join several data for Ml model and train
5. Score_estimation  - score and shape

"""
 if __name__ = 'main':
    df_train, df_test, bureau, bur_balance, credit_card, instal_pay, Posh_card = extract.open_and_create_data()
    df_train, df_test, buro = transform.transform_cat_feature(df_train, df_test, buro)
    target, train = transform.create_train(df_train)
    train, test, buro = features_create.new_feature(train, df_test, buro)
    train, test = ml_train.prepare_data_model(train, test, buro)
    predict, model = ml_train.model_fit(train, test, target)
    score.accuracy_score(predict, target)
    score.shape_ml(model, train, test)
