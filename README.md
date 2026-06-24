# House Price Prediction

## Project Overview
This project uses Machine Learning techniques to predict house prices based on various housing features. The goal is to build a predictive model that can estimate property prices accurately and help understand the factors affecting house values.

## Objectives
- Analyze housing market data.
- Clean and preprocess the dataset.
- Perform Exploratory Data Analysis (EDA).
- Visualize important trends and relationships.
- Train and evaluate machine learning models.
- Predict house prices based on property features.

## Dataset
The dataset contains information about residential properties and their prices.

### Features
- Area
- Number of Bedrooms
- Number of Bathrooms
- Floors
- Parking
- Furnishing Status
- Air Conditioning
- Preferred Area
- Price (Target Variable)

Dataset File:
- `Housing.csv`

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Workflow

### 1. Data Collection
Loaded the housing dataset and inspected its structure.

### 2. Data Cleaning
- Checked for missing values.
- Removed inconsistencies.
- Converted categorical variables into numerical format.

### 3. Exploratory Data Analysis (EDA)
- Distribution of house prices.
- Correlation analysis.
- Feature relationship visualization.
- Price comparison across categories.

### 4. Model Building
Machine Learning algorithms were applied to predict house prices.

### 5. Model Evaluation
The model was evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Results
The model successfully predicts house prices using property features and provides insights into the factors influencing housing costs.

## Repository Structure

```text
House_Price_Prediction/
│
├── Housing.csv
├── analysis.ipynb
├── charts/
├── summary.docx
├── summary.pdf
└── README.md
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/House_Price_Prediction.git
```

2. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

3. Open the notebook

```bash
jupyter notebook analysis.ipynb
```

4. Run all cells to reproduce the analysis and predictions.

## Future Improvements
- Hyperparameter tuning.
- Testing advanced regression models.
- Deployment as a web application.
- Real-time property price prediction.

## Author
**Pratap Kumar Mishra**

## License
This project is developed for educational and internship purposes only.
