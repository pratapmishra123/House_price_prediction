# 🏠 House Price Prediction Dashboard

A machine learning-powered House Price Prediction system with an interactive Streamlit dashboard for predicting property prices and visualizing model insights.

## 🚀 Project Overview

This project predicts house prices using a Linear Regression model trained on housing data and provides a professional dashboard for users to:

- Predict house prices based on property features
- Visualize data distributions
- Analyze feature relationships
- Compare actual vs predicted values
- Explore model insights interactively

---

## 📊 Dashboard Features

### Prediction Module
- Area (sq.ft) input
- Bedrooms selection
- Bathrooms selection
- Stories selection
- Parking spaces selection
- Real-time predicted house price
- Price per square foot calculation

### Analytics Module
- House price distribution visualization
- Actual vs predicted comparison chart
- Feature correlation heatmap
- Model insights section

### UI Features
- Clean professional interface
- Interactive sidebar controls
- KPI metrics cards
- Responsive dashboard layout

---

## 🛠️ Tech Stack

**Frontend**
- Streamlit

**Machine Learning**
- Scikit-learn
- Linear Regression

**Data Processing**
- Pandas
- NumPy

**Visualization**
- Matplotlib
- Seaborn

---

## 📁 Project Structure

```bash
House_price_prediction/
│
├── house_dashboard_app.py
├── Housing.csv
├── model.pkl
├── chart1_price_distribution.png
├── chart2_correlation_heatmap.png
├── chart3_actual_vs_predicted.png
├── analysis.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/pratapmishra123/House_price_prediction.git
```

Move into the project folder:

```bash
cd House_price_prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Launch Streamlit:

```bash
streamlit run house_dashboard_app.py
```

The application will run locally at:

```bash
http://localhost:8501
```

---

## 📈 Machine Learning Workflow

1. Data preprocessing
2. Feature engineering
3. Train-test split
4. Linear Regression model training
5. Model evaluation
6. Dashboard integration

---

## 📊 Model Evaluation

Metrics used:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

Visual evaluation:

- Actual vs Predicted plot
- Correlation Heatmap
- Price Distribution analysis

---

## Future Improvements

- Add Random Forest and XGBoost models
- Add deployment support
- Add map-based property visualization
- Connect live datasets
- Add price trend forecasting

---

## 👨‍💻 Author

**Pratap Kumar Mishra**

GitHub: https://github.com/pratapmishra123

---

## ⭐ If you found this project useful, consider giving it a star.
