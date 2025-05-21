# 🏡 Bangalore House Price Predictor

An AI-powered Streamlit web application to predict house prices in Bangalore based on area, BHK, bathroom count, and location — designed with a modern real-estate-themed frontend.


---

## 📌 Overview

This project uses machine learning (Linear Regression) to provide price estimates for properties in Bangalore. It includes a modern, themed landing page, an interactive prediction form, and a smart fallback system for suggesting similar listings.

---

## 🚀 Key Features

- 🎯 Predict housing prices using a trained Linear Regression model
- 📍 Location, BHK, Bathroom & Area inputs via an elegant form
- 💡 Shows similar properties and handles fallback if none match
- ✨ Custom landing page styled like a real estate platform
- 🧠 Data cleaning, feature engineering, and one-hot encoding

---

## 📁 Folder Structure

```
bangalore_price_app/
├── app.py                            # Main Streamlit app
├── app_themed.py                     # Themed version with styled hero section
├── model/
│   ├── banglore_home_prices_model.joblib
│   └── columns.json
├── data/
│   └── bengaluru_house_prices.csv
├── notebooks/
│   └── banglore_home_prices_final.ipynb
├── utils.py                          # Reusable predict function
├── requirements.txt
└── README.md
```

---

## 🛠 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/mep3175/bangalore-house-price-prediction.git
cd bangalore-house-price-prediction
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Launch the app
```bash
streamlit run app.py
# or run the themed version:
streamlit run app_themed.py
```

---

## 💡 How It Works

- The model uses `LinearRegression` trained on real housing data.
- Location is one-hot encoded using the same structure from `columns.json`.
- Predictions are based on user input and compared against actual data for similar listings.
- If no listing is found in the selected location, the app shows suggestions from nearby areas with the same BHK and area range.

---

## 🖼 UI Preview

| Landing Page | Prediction Form |
|--------------|-----------------|


---

## 👨‍💻 Author

Built by **Meet Patel**  
📫 [LinkedIn](https://www.linkedin.com/in/erpatelmeet) • 🌐 [GitHub](https://github.com/mep3175)

---

## 📄 License

This project is licensed for educational and personal use. Feel free to use or modify with credit.
