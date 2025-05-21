import streamlit as st
import joblib
import json
import numpy as np
import pandas as pd

st.set_page_config(page_title="Bangalore House Price Predictor", layout="wide")

# Load model and metadata
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

st.markdown("""
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 900;
            color: #EA4C89;
            margin-bottom: 0;
        }
        .sub-title {
            font-size: 22px;
            color: #5A5A5A;
            margin-top: 0;
            margin-bottom: 20px;
        }
        .cta-btn {
            background: linear-gradient(to right, #EA4C89, #623CEA);
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
            border-radius: 30px;
            text-decoration: none;
        }
        .hero-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #F8F8FF;
            padding: 3rem 2rem;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='hero-section'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<p class='main-title'>FIND YOUR<br>DREAM HOME</p>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>Use AI to predict realistic property prices in Bangalore based on your preferences.</p>", unsafe_allow_html=True)
        st.markdown("<a href='#prediction-form' class='cta-btn'>More Info</a>", unsafe_allow_html=True)
    with col2:
        st.image("https://img.freepik.com/free-photo/house-model-with-real-estate-agent_23-2150709962.jpg", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.header("🏠 Price Prediction Form")
st.markdown('<div id="prediction-form"></div>', unsafe_allow_html=True)

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

if 'predicted_price' in st.session_state:
    price = st.session_state['predicted_price']
    location, sqft, bath, bhk = st.session_state['inputs']
    st.success(f"Estimated Price: ₹ {price} Lakhs")

    st.subheader("💡 Similar Properties")
    filtered = raw_df[
        (raw_df['location'].str.lower() == location.lower()) &
        (raw_df['bhk'] == bhk) &
        (raw_df['total_sqft'].between(sqft - 200, sqft + 200))
    ]

    if filtered.empty:
        st.info("No similar properties found in this location. Showing similar properties from other areas.")
        filtered = raw_df[
            (raw_df['bhk'] == bhk) &
            (raw_df['total_sqft'].between(sqft - 200, sqft + 200))
        ]

    st.dataframe(filtered[['location', 'total_sqft', 'bath', 'bhk', 'price']].head(10))

st.caption("Built by Meet Patel ✨")
