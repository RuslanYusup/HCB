import pandas as pd

"""
Допустим, что источник данных находится на папке с известных сервером
В данном скрипте данные загружаются 

"""
def open_and_create_data(): #подскажи нужно ли что-либо передавать сюда?
    df_train = pd.read_csv(r'C:\Users\user\Desktop\HCB\application_train.csv)
    df_test = pd.read_csv(r'C:\Users\user\Desktop\HCB\application_test.csv')

    bureau = pd.read_csv('bureau.csv')

    bur_balance = pd.read_csv(r'C:\Users\user\Desktop\HCB\bureau_balance.csv')
    credit_card = pd.read_csv(r'C:\Users\user\Desktop\HCB\credit_card_balance.csv')
    instal_pay = pd.read_csv(r'C:\Users\user\Desktop\HCB\installments_payments.csv')
    Posh_card = pd.read_csv(r'C:\Users\user\Desktop\HCB\POS_CASH_balance.csv')

return df_train, df_test, bureau, bur_balance, credit_card, instal_pay, Posh_card
