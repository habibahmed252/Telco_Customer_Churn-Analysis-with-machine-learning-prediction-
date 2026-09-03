import streamlit as st
import pandas as pd
import joblib

# =========================
# Page Setup
# =========================

st.set_page_config(
    page_title="Telco Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# =========================
# Custom Dark Theme
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #17120f, #241914, #302019);
    color: #f5eee8;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 1rem;
}

h1, h2, h3 {
    color: #f3dfcf !important;
}

.hero {
    text-align: center;
    padding: 25px;
    background: rgba(65, 45, 34, 0.65);
    border: 1px solid #76533f;
    border-radius: 20px;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 38px;
    font-weight: 700;
    color: #ead0bc;
}

.hero-text {
    color: #cdb9aa;
    font-size: 16px;
}

.card {
    background: #261b16;
    border: 1px solid #684937;
    border-radius: 18px;
    padding: 22px;
    margin-top: 20px;
}

.result-card {
    background: linear-gradient(135deg, #33231b, #211713);
    border: 1px solid #916b50;
    border-radius: 22px;
    padding: 28px;
    text-align: center;
    margin-top: 25px;
}

.probability {
    font-size: 48px;
    font-weight: 800;
    color: #e5c2a7;
}

.risk {
    font-size: 24px;
    font-weight: 700;
    margin-top: 8px;
}

.footer {
    text-align: center;
    color: #9f8878;
    margin-top: 35px;
    padding-top: 15px;
    border-top: 1px solid #4d372b;
    font-size: 14px;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 48px;
    background: #8b6248;
    color: white;
    border: none;
    font-size: 17px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #a97858;
}

</style>
""", unsafe_allow_html=True)


# =========================
# Load Model
# =========================

model = joblib.load("telco_churn_model.pkl")


# =========================
# Welcome Section
# =========================

st.markdown("""
<div class="hero">

<div class="hero-title">
📊 Telco Customer Churn
</div>

<div class="hero-text">
Welcome! Enter customer information below to estimate
the probability of customer churn.
</div>

</div>
""", unsafe_allow_html=True)


# =========================
# Customer Information
# =========================

st.markdown(
    '<div class="card"><h3>👤 Customer Information</h3></div>',
    unsafe_allow_html=True
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=72,
    value=12
)

phone = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    [
        "Security Enabled",
        "No Security",
        "No internet service"
    ]
)

online_backup = st.selectbox(
    "Online Backup",
    [
        "Backup Enabled",
        "No Online Backup",
        "No Internet Service"
    ]
)

device_protection = st.selectbox(
    "Device Protection",
    [
        "Protection Enabled",
        "No Device Protection",
        "No Internet Service"
    ]
)

tech_support = st.selectbox(
    "Tech Support",
    [
        "HasTech Support",
        "No Tech Support",
        "No Internet Service"
    ]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    [
        "Streaming TV",
        "No Streaming TV",
        "No Internet Service"
    ]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    [
        "Streaming Movies",
        "No Streaming Movies",
        "No Internet Service"
    ]
)

contract = st.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=18.25,
    max_value=118.75,
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=18.80,
    max_value=8684.80,
    value=1000.0
)


# =========================
# Prediction
# =========================

st.write("")

if st.button("✨ Analyze Customer"):

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen statue": senior,
        "Dependents": dependents,
        "Partner": partner,
        "Phone Service": phone,
        "tenure": tenure,
        "Having Multiple Lines": multiple_lines,
        "InternetService": internet,
        "Online Security": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "Tech Support Service": tech_support,
        "Streaming TV Service": streaming_tv,
        "Streaming Movies Service": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    probability = model.predict_proba(customer)[0][1]

    percentage = probability * 100

    # Risk
    if probability < 0.30:
        risk = "Low Risk"
        icon = "🟢"
    elif probability < 0.60:
        risk = "Medium Risk"
        icon = "🟠"
    else:
        risk = "High Risk"
        icon = "🔴"

    # =========================
    # Result
    # =========================

    st.markdown(f"""
    <div class="result-card">

        <h2>Prediction Result</h2>

        <div class="probability">
            {percentage:.1f}%
        </div>

        <p style="color:#bfa99a;">
            Estimated Churn Probability
        </p>

        <div class="risk">
            {icon} {risk}
        </div>

    </div>
    """, unsafe_allow_html=True)

    # Visual probability bar
    st.write("")
    st.progress(float(probability))

    if probability < 0.30:
        st.success("This customer currently shows a relatively low churn risk.")
    elif probability < 0.60:
        st.warning("This customer shows a moderate churn risk and may need attention.")
    else:
        st.error("This customer shows a high churn risk and may require retention action.")


# =========================
# Footer
# =========================

st.markdown("""
<div class="footer">
Created by <b>Eng. Habiba Ahmed</b>
<br>
Telco Customer Churn Prediction
</div>
""", unsafe_allow_html=True)
