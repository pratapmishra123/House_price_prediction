import streamlit as st
from PIL import Image
import os

# ------------------------------
# Page configuration
# ------------------------------

st.set_page_config(
    page_title="House Price Prediction Dashboard",
    layout="wide"
)

# ------------------------------
# Header
# ------------------------------

st.title("🏠 House Price Prediction Dashboard")
st.markdown(
    "Professional dashboard for house price prediction and model analysis"
)

st.divider()

# ------------------------------
# Sidebar inputs
# ------------------------------

st.sidebar.header("House Details")

area = st.sidebar.slider(
    "Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=2500
)

bedrooms = st.sidebar.slider(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.sidebar.slider(
    "Bathrooms",
    min_value=1,
    max_value=8,
    value=2
)

stories = st.sidebar.slider(
    "Stories",
    min_value=1,
    max_value=5,
    value=2
)

parking = st.sidebar.slider(
    "Parking Spaces",
    min_value=0,
    max_value=5,
    value=1
)

# ------------------------------
# Demo prediction
# Replace later with model.pkl
# ------------------------------

predicted_price = (
    3500000
    + (area * 500)
    + (bedrooms * 100000)
    + (bathrooms * 75000)
)

price_per_sqft = predicted_price / area

# ------------------------------
# KPI Metrics
# ------------------------------

st.subheader("Prediction Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Predicted Price",
        value=f"₹ {predicted_price:,.0f}"
    )

with col2:
    st.metric(
        label="Price per Sq.Ft",
        value=f"₹ {price_per_sqft:,.0f}"
    )

with col3:
    st.metric(
        label="Model",
        value="Linear Regression"
    )

st.divider()

# ------------------------------
# Image display function
# ------------------------------

def display_image(filename, title):

    st.subheader(title)

    if os.path.isfile(filename):

        image = Image.open(filename)

        st.image(
            image,
            width=600
        )

    else:

        st.warning(
            f"{filename} not found.\n"
            f"Place this file in the same folder as house_dashboard_app.py"
        )

# ------------------------------
# Charts section
# ------------------------------

col1, col2 = st.columns(2)

with col1:

    display_image(
        "chart1_price_distribution.png",
        "House Price Distribution"
    )

with col2:

    display_image(
        "chart3_actual_vs_predicted.png",
        "Actual vs Predicted"
    )

st.divider()

display_image(
    "chart2_correlation_heatmap.png",
    "Correlation Heatmap"
)

st.divider()

# ------------------------------
# Insights
# ------------------------------

st.subheader("📊 Model Insights")

st.info("""
• Area has a strong positive relationship with price

• Bathrooms and bedrooms increase predicted value

• Preferred location contributes significantly

• Linear Regression predictions align reasonably with actual values

• Correlation heatmap identifies important features
""")

# ------------------------------
# Footer
# ------------------------------

st.markdown("---")
st.caption(
    "Created by Pratap Kumar Mishra"
)