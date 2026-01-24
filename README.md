# House Price Prediction using Machine Learning
## Project Overview
This project focuses on predicting house prices using the Boston Housing Dataset.  
Multiple regression models were trained, tuned, and evaluated, followed by an advanced stacking approach to improve predictive performance. The project follows a complete end-to-end machine learning pipeline, from data understanding to final evaluation.

---

## 📂 Project Structure
HOUSE_PRICE_PREDICTION/
│
├── datasets/
│ └── boston_dataset.csv 
│ └── boston_cleaned.csv 
│ └── final_boston.csv   
│ └── trails.csv         
│
├── models/
│ └── stacking_model.pkl
│
├── data_understanding.ipynb
├── eda.ipynb
├── cleaning.ipynb
├── feature_engineering.ipynb
├── modeling_baseline.ipynb
├── optuna_tuning.ipynb
├── ensembles_stacking.ipynb
├── final_evaluation.ipynb
│
├── requirements.txt
└── README.md

---

## Dataset Description
- **Dataset**: Boston Housing Dataset  
- **Target Variable**: `MEDV` (Median house value in $1000s)  
- **Features**: Crime rate, number of rooms, pollution levels, accessibility, tax rate, etc.

---

## Technologies & Libraries Used
- Python
- NumPy
- Pandas
- Matplotlib & Seaborn
- Scikit-learn
- XGBoost
- Optuna
- Joblib

---

## Methodology

### 1️ Data Understanding
- Dataset loading
- Data shape and types
- Feature meaning analysis
- Basic statistical summary

### 2️ Data Cleaning
- Outlier detection and treatment
- Data consistency checks

### 3️ Exploratory Data Analysis (EDA)
- Feature distributions
- Correlation analysis
- Feature vs target relationships
- Multicollinearity checks

### 5️ Baseline Modeling
Trained initial regression models:
- Linear Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

---

## Hyperparameter Tuning (Optuna)
- Optuna was used to tune:
  - Random Forest
  - Gradient Boosting
  - XGBoost
- Optimization metric: **R² Score**
- Cross-validation used to ensure generalization

---

## Stacking
A stacking regressor was built using:
- **Base models**:
  - Random Forest
  - Gradient Boosting
  - XGBoost
- **Meta-model**:
  - Ridge Regression

This approach improved overall predictive performance compared to individual models.

---

## Final Evaluation
The final model was evaluated using:
- R² Score
- RMSE
- MAE

### Diagnostic Plots:
- Actual vs Predicted values
- Residuals vs Predicted values
- Residual distribution
- Model comparison (R²)

---

## Model Saving & Reuse
The final trained model was saved using `joblib` and reused in a separate notebook for evaluation without retraining also 3 best models of each Random Forest, Gradient Boosting and XGBoost are saved and used in final_evaluation notebook.

## Result
The stacking model achieved the best performance with the highest R² score

## Conclusion
This project demonstrates a complete machine learning workflow for regression problems, highlighting the effectiveness of stacking techniques in improving predictive performance

## Author
### Chirag Poojary
Machine Learning Project – House Price Prediction