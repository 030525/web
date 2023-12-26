


def predict_to_csv(csv,rows=None,target):

    def predict_(csv,rows):

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


