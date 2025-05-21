import json
import numpy as np
import joblib

model = joblib.load("model/banglore_home_prices_model.joblib")
with open("model/columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

def predict_price(location, sqft, bath, bhk):
    x = [0] * len(data_columns)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location.lower() in data_columns:
        loc_index = data_columns.index(location.lower())
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)
