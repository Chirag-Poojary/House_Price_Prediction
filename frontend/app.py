import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"
st.title("House Price Prediction App")
st.markdown("Enter the features of the house below to predict its price.")

CRIM = st.number_input("CRIM: Per capita crime rate by town", value=0.0)
ZN = st.number_input("ZN: Proportion of residential land zoned for lots over 25,000 sq.ft.", value=0.0)
INDUS = st.number_input("INDUS: Proportion of non-retail business acres per town", value=0.0)
CHAS = st.selectbox("CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)", options=[0, 1])
NOX = st.number_input("NOX: Nitric oxides concentration (parts per 10 million)", value=0.0)
RM = st.number_input("RM: Average number of rooms per dwelling", value=0.0)
AGE = st.number_input("AGE: Proportion of owner-occupied units built prior to 1940", value=0.0)
DIS = st.number_input("DIS: Weighted distances to five Boston employment centers", value=0.0)
RAD = st.selectbox("RAD: Index of accessibility to radial highways", options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
TAX = st.number_input("TAX: Full-value property tax rate per $10,000", value=0.0)
PTRATIO = st.number_input("PTRATIO: Pupil-teacher ratio by town", value=0.0)
B = st.number_input("B: 1000(Bk - 0.63)^2 where Bk is the proportion of Black people by town", value=0.0)   
LSTAT = st.number_input("LSTAT: Percentage of lower status population", value=0.0)

if st.button("Predict Price"):
    features = {
        "CRIM": CRIM,
        "ZN": ZN,
        "INDUS": INDUS,
        "CHAS": CHAS,
        "NOX": NOX,
        "RM": RM,
        "AGE": AGE,
        "DIS": DIS,
        "RAD": RAD,
        "TAX": TAX,
        "PTRATIO": PTRATIO,
        "B": B,
        "LSTAT": LSTAT
    }
    try:
        response = requests.post(API_URL, json=features)
        if response.status_code == 200:
            predicted_price = response.json().get("predicted_price")
            st.success(f"Predicted House Price: ${predicted_price*1000:.2f}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
