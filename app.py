import streamlit as st
import numpy as np
import joblib

st.title("Customer Churn Prediction Demo")

# Load model and scaler
clf = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

st.header("Enter Customer Details")

# Feature input fields (order must match model training)
gender = st.selectbox(
    "Gender", [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male",
    help="Customer's gender"
)
senior = st.selectbox(
    "Senior Citizen", [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes",
    help="Is the customer a senior citizen?"
)
partner = st.selectbox(
    "Partner", [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes",
    help="Does the customer have a partner?"
)
dependents = st.selectbox(
    "Dependents", [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes",
    help="Does the customer have dependents?"
)
tenure = st.slider(
    "Tenure (months)", 0, 72, 12,
    help="Number of months the customer has stayed"
)
phoneservice = st.selectbox(
    "Phone Service", [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes",
    help="Does the customer have phone service?"
)
multiplelines = st.selectbox(
    "Multiple Lines", [0, 1, 2],
    format_func=lambda x: ["No", "No phone service", "Yes"][x],
    help="Does the customer have multiple lines?"
)
internetservice = st.selectbox(
    "Internet Service", [0, 1, 2],
    format_func=lambda x: ["DSL", "Fiber optic", "No"][x],
    help="Type of internet service"
)
onlinesecurity = st.selectbox(
    "Online Security", [0, 1, 2],
    format_func=lambda x: ["No", "No internet service", "Yes"][x],
    help="Does the customer have online security?"
)
onlinebackup = st.selectbox(
    "Online Backup", [0, 1, 2],
    format_func=lambda x: ["No", "No internet service", "Yes"][x],
    help="Does the customer have online backup?"
)
deviceprotection = st.selectbox(
    "Device Protection", [0, 1, 2],
    format_func=lambda x: ["No", "No internet service", "Yes"][x],
    help="Does the customer have device protection?"
)
techsupport = st.selectbox(
    "Tech Support", [0, 1, 2],
    format_func=lambda x: ["No", "No internet service", "Yes"][x],
    help="Does the customer have tech support?"
)
streamingtv = st.selectbox(
    "Streaming TV", [0, 1, 2],
    format_func=lambda x: ["No", "No internet service", "Yes"][x],
    help="Does the customer have streaming TV?"
)
streamingmovies = st.selectbox(
    "Streaming Movies", [0, 1, 2],
    format_func=lambda x: ["No", "No internet service", "Yes"][x],
    help="Does the customer have streaming movies?"
)
contract = st.selectbox(
    "Contract", [0, 1, 2],
    format_func=lambda x: ["Month-to-month", "One year", "Two year"][x],
    help="Customer's contract type"
)
paperlessbilling = st.selectbox(
    "Paperless Billing", [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes",
    help="Does the customer use paperless billing?"
)
paymentmethod = st.selectbox(
    "Payment Method", [0, 1, 2, 3],
    format_func=lambda x: [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ][x],
    help="Customer's payment method"
)
monthlycharges = st.number_input(
    "Monthly Charges", 0.0, 200.0, 70.0,
    help="The amount charged to the customer monthly"
)
totalcharges = st.number_input(
    "Total Charges", 0.0, 10000.0, 1000.0,
    help="The total amount charged to the customer"
)

# Arrange features in the correct order
features = np.array([[
    gender, senior, partner, dependents, tenure, phoneservice, multiplelines,
    internetservice, onlinesecurity, onlinebackup, deviceprotection, techsupport,
    streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod,
    monthlycharges, totalcharges
]])

features_scaled = scaler.transform(features)

if st.button("Predict Churn"):
    pred = clf.predict(features_scaled)[0]
    st.success("Prediction: {}".format("Churn" if pred == 1 else "No Churn"))