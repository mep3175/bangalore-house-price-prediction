# 🏡 Bangalore House Price Predictor

A modern, AI-powered web app built with Streamlit that estimates housing prices in Bangalore using area, BHK, bathroom count, and location. Styled like a real estate platform landing page.

![Hero Banner](https://img.freepik.com/free-photo/house-model-with-real-estate-agent_23-2150709962.jpg)

---

## 🚀 Features

- ✅ Predicts property prices using a trained Linear Regression model
- 🧠 Inputs: Area (sqft), BHK, Bathrooms, and Location
- 📊 Suggests similar listings (based on location, BHK, area)
- 🪄 Smart fallback when no nearby match is found
- 🎨 Beautiful themed landing page (HTML + CSS in Streamlit)

---

## 📁 Project Structure

```
bangalore_price_app/
├── app.py                            # Main themed app
├── model/
│   ├── banglore_home_prices_model.joblib
│   └── columns.json
├── data/
│   └── bengaluru_house_prices.csv
├── notebooks/
│   └── banglore_home_prices_final.ipynb
├── utils.py                          # Predict function
├── requirements.txt
└── README.md                         # You're here
```

---

## 🛠 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Launch the Streamlit app
streamlit run app.py
```

---

## 📊 Model Info

- Trained using `LinearRegression` on cleaned Bangalore housing dataset
- Uses one-hot encoded locations
- Only requires `joblib`, `pandas`, `scikit-learn`, `streamlit`, `numpy`

---

## 🖼 App UI Preview

| Dream Home Hero Section | Prediction Form |
|-------------------------|-----------------|
| ![Hero](https://img.freepik.com/free-photo/house-model-with-real-estate-agent_23-2150709962.jpg) | ![Form](https://via.placeholder.com/300x120.png?text=Streamlit+Form) |

---

## 👨‍💻 Author

Built by **Meet Patel** ✨  
📫 [LinkedIn → erpatelmeet](https://www.linkedin.com/in/erpatelmeet)

---

## 📄 License

This project is intended for personal and academic use. Feel free to remix with credit.

---
