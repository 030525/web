import pandas as pd


def read(csv,rows):
    train_df = pd.read_csv(csv,nrows=rows)

    # drop useless cols
    train_df = train_df.drop(columns=['Customer_ID','SSN'])
    
    # encoded text
    train_df_encoded = pd.get_dummies(train_df)

    return train_df_encoded

def Xy(csv,rows):
    train_df_encoded = read(csv,rows) 

    X = train_df_encoded
    y = None
    
    try:
        X = train_df_encoded.drop(columns=['Credit_Score_Poor','Credit_Score_Standard','Credit_Score_Good'])
        y = train_df_encoded[['Credit_Score_Poor','Credit_Score_Standard','Credit_Score_Good']]
    finally:
        return X,y


