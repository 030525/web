import pandas as pd


def read(csv,rows = None):
    train_df=None

    if rows is None:
        train_df = pd.read_csv(csv)
    else:
        train_df = pd.read_csv(csv,nrows=rows)

    # drop useless cols
    train_df = train_df.drop(columns=['Customer_ID','SSN','ID'])
    
    # encoded text
    train_df_encoded = pd.get_dummies(train_df)

    return train_df_encoded

def Xy(csv,rows = None):
    train_df_encoded = read(csv,rows) 

    X = train_df_encoded.drop(columns=['Credit_Score_Poor','Credit_Score_Standard','Credit_Score_Good'])
    y = train_df_encoded[['Credit_Score_Poor','Credit_Score_Standard','Credit_Score_Good']]

    return X,y
