import joblib
import pandas as pd
import ast

def read_list(fp):
    file_path = fp
    with open(file_path, 'r') as file:
        file_content = file.read()

    return ast.literal_eval(file_content)


def predict_to_csv(csv,rows=None,target):

    def predict_(csv,rows):
        feature_need = read_list('x')

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

        def fill_missing_features(predict):
            gap = set(feature_need) - set(predict.columns)

            for i in gap:
                predict[i] = 0
        
        def delete_unique_features(predict):
            gap = list(set(predict.columns) - set(feature_need))

            predict.drop(columns=gap, inplace=True)

        def fill_missing_value(predict):
            from sklearn.model_selection import train_test_split
            from sklearn.impute import SimpleImputer

            imp = SimpleImputer(strategy='mean')
            imp_train = imp.fit(predict)
            predict = imp_train.transform(predict)

        def decode(predictions):
            y = read_list('y')
            df = pd.DataFrame(predictions, columns=y)
            result = df.apply(lambda row: ', '.join([label.replace('Credit_Score_', '') for idx, label in enumerate(y) if row.values[idx]]), axis=1)

            df['Credit_Score'] = result

            return df['Credit_Score']

        data = read(csv,rows)
        fill_missing_value(data)
        fill_missing_features(data)
        delete_unique_features(data)

        model = joblib.load('decision_tree_model.joblib')
        predictions = model.predict(data)
        return decode(predictions)

    def to_csv_(target,feature,data):
        train_df = pd.read_csv(csv,nrows=rows)
        train_df[feature]=predict(data)
        train_df.to_csv(target, index=False)




predict_csv("../data/test.csv",200)


