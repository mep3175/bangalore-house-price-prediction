import streamlit as st
import joblib
import json
import numpy as np
import pandas as pd

st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")

model = joblib.load("model/banglore_home_prices_model.joblib")
with open("model/columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]
locations = data_columns[3:]

def predict_price(location, sqft, bath, bhk):
    x = [0] * len(data_columns)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location.lower() in data_columns:
        loc_index = data_columns.index(location.lower())
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)

@st.cache_data
def load_data():
    return pd.read_csv("data/bengaluru_house_prices.csv")

raw_df = load_data()
raw_df = raw_df.dropna()
raw_df['bhk'] = raw_df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else None)
raw_df = raw_df[raw_df['bhk'].notnull()]
raw_df['total_sqft'] = raw_df['total_sqft'].apply(lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else None)
raw_df = raw_df[raw_df['total_sqft'].notnull()]

st.title("🏡 Bangalore House Price Predictor")
st.write("Estimate property prices based on area, location, BHK and bathroom count")

with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        sqft = st.number_input("Total Area (in sqft)", min_value=300, max_value=10000, step=50)
        bath = st.selectbox("Bathrooms", options=[1, 2, 3, 4, 5])
    with col2:
        bhk = st.selectbox("BHK", options=[1, 2, 3, 4, 5])
        location = st.selectbox("Location", sorted(locations))
    submitted = st.form_submit_button("Predict Price")
    reset = st.form_submit_button("Reset Form")

if submitted:
    price = predict_price(location, sqft, bath, bhk)
    st.session_state['predicted_price'] = price
    st.session_state['inputs'] = (location, sqft, bath, bhk)

if reset:
    st.session_state.pop('predicted_price', None)
    st.session_state.pop('inputs', None)
    st.rerun()

# Show result if prediction was submitted
if 'predicted_price' in st.session_state:
    price = st.session_state['predicted_price']
    st.success(f"Estimated Price: ₹ {price} Lakhs")

    location, sqft, bath, bhk = st.session_state['inputs']
    st.subheader("💡 Similar Properties")
    filtered = raw_df[
        (raw_df['location'].str.lower() == location.lower()) &
        (raw_df['bhk'] == bhk) &
        (raw_df['total_sqft'].between(sqft - 200, sqft + 200))
    ]
    st.dataframe(filtered[['location', 'total_sqft', 'bath', 'bhk', 'price']].head(10))


st.caption("Built by Meet Patel ✨")
