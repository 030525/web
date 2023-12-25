import joblib
import pandas as pd

model = joblib.load('decision_tree_model.joblib')

def output(data):
    prediction = model.predict(data)

    print("Prediction for the user:", prediction[0])