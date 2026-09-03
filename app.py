
import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Telco Churn AI",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM DARK BLUE THEME
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, Helvetica, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(0, 119, 255, 0.10), transparent 28%),
        radial-gradient(circle at 85% 20%, rgba(0, 119, 255, 0.08), transparent 25%),
        #05070b;
    color: #ffffff;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ---------------- HEADER ---------------- */

.hero {
    background: linear-gradient(
        135deg,
        rgba(13, 19, 30, 0.98),
        rgba(7, 12, 20, 0.98)
    );

    border: 1px solid rgba(0, 136, 255, 0.35);
    border-radius: 24px;

    padding: 42px 30px;
    margin-bottom: 28px;

    text-align: center;

    box-shadow:
        0 15px 45px rgba(0, 0, 0, 0.45),
        0 0 35px rgba(0, 119, 255, 0.07);
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #ffffff;
    margin-bottom: 10px;
}

.hero-title span {
    color: #1697ff;
}

.hero-text {
    font-size: 17px;
    color: #aeb9c8;
    line-height: 1.7;
}

/* ---------------- SECTION HEADERS ---------------- */

.section-title {
    color: #ffffff;
    font-size: 23px;
    font-weight: 750;
    margin-top: 25px;
    margin-bottom: 15px;
}

.section-line {
    height: 2px;
    width: 65px;
    background: #1494ff;
    margin-top: -8px;
    margin-bottom: 20px;
    border-radius: 5px;
}

/* ---------------- INPUTS ---------------- */

div[data-baseweb="select"] > div {
    background-color: #0c1119 !important;
    border: 1px solid #263241 !important;
    border-radius: 10px !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: #168fff !important;
}

.stNumberInput input {
    background-color: #0c1119 !important;
    color: #ffffff !important;
    border: 1px solid #263241 !important;
    border-radius: 10px !important;
}

label {
    color: #d7e0ea !important;
    font-weight: 600 !important;
}

/* ---------------- BUTTON ---------------- */

div.stButton {
    margin-top: 28px;
}

div.stButton > button {
    width: 100%;
    height: 58px;

    border-radius: 13px;

    background: linear-gradient(
        90deg,
        #0077ff,
        #129dff
    );

    color: white;

    border: none;

    font-size: 18px;
    font-weight: 750;

    box-shadow:
        0 8px 25px rgba(0, 119, 255, 0.22);

    transition: 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 30px rgba(0, 119, 255, 0.35);
}

/* ---------------- RESULT CARD ---------------- */

.result-card {
    background:
        linear-gradient(
            145deg,
            rgba(10, 19, 31, 0.98),
            rgba(5, 10, 17, 0.98)
        );

    border: 1px solid rgba(20, 148, 255, 0.45);

    border-radius: 24px;

    padding: 35px 25px;

    margin-top: 30px;

    text-align: center;

    box-shadow:
        0 15px 50px rgba(0, 0, 0, 0.45),
        0 0 35px rgba(0, 119, 255, 0.08);
}

.result-title {
    color: #ffffff;
    font-size: 27px;
    font-weight: 750;
}

.probability {
    color: #1697ff;
    font-size: 56px;
    font-weight: 850;
    margin-top: 12px;
}

.probability-label {
    color: #9ba9b8;
    font-size: 15px;
}

.risk {
    color: #ffffff;
    font-size: 25px;
    font-weight: 750;
    margin-top: 18px;
}

/* ---------------- INFO CARDS ---------------- */

.info-card {
    background: #0a0f16;
    border: 1px solid #202b38;
    border-radius: 17px;
    padding: 20px;
    margin-top: 18px;
}

.info-title {
    color: #1494ff;
    font-size: 14px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.info-value {
    color: #ffffff;
    font-size: 25px;
    font-weight: 750;
    margin-top: 5px;
}

/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;

    margin-top: 55px;
    padding: 25px 10px 10px;

    border-top: 1px solid #1e2935;

    color: #8794a3;

    font-size: 15px;
}

.footer-name {
    color: #ffffff;
    font-size: 20px;
    font-weight: 800;
    margin-top: 7px;
}

.footer-name span {
    color: #1697ff;
}

.footer-project {
    margin-top: 7px;
    color: #657384;
    font-size: 13px;
}

/* ---------------- PROGRESS ---------------- */

div[data-testid="stProgress"] > div > div {
    background-color: #1494ff !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("telco_churn_model.pkl")


try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the trained model.")
    st.stop()


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-title">
        Telco Customer <span>Churn AI</span>
    </div>

    <div class="hero-text">
        Intelligent customer churn prediction powered by
        Machine Learning and XGBoost.
        <br>
        Enter customer information below to estimate churn risk.
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.markdown("""
<div class="section-title">Customer Information</div>
<div class="section-line"></div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
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
        value=12,
        step=1
    )

    phone = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )


with col2:

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
        "Tech Support Service",
        [
            "HasTech Support",
            "No Tech Support",
            "No Internet Service"
        ]
    )


with col3:

    streaming_tv = st.selectbox(
        "Streaming TV Service",
        [
            "Streaming TV",
            "No Streaming TV",
            "No Internet Service"
        ]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies Service",
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
        min_value=0.0,
        max_value=20000.0,
        value=70.0,
        step=1.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=50000.0,
        value=1000.0,
        step=10.0
    )


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button("Analyze Customer"):

    try:

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

        # Make sure columns are in exactly the same order
        # used during model training.
        customer = customer[model.feature_names_in_]

        probability = model.predict_proba(customer)[0][1]

        percentage = probability * 100

        # Risk classification
        if probability < 0.30:
            risk = "Low Risk"
            icon = "LOW"
        elif probability < 0.60:
            risk = "Medium Risk"
            icon = "MEDIUM"
        else:
            risk = "High Risk"
            icon = "HIGH"

        # ====================================================
        # RESULT
        # ====================================================

        st.markdown(f"""
        <div class="result-card">

            <div class="result-title">
                Prediction Result
            </div>

            <div class="probability">
                {percentage:.1f}%
            </div>

            <div class="probability-label">
                Estimated Customer Churn Probability
            </div>

            <div class="risk">
                {icon} &nbsp; {risk}
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.progress(float(probability))

        # Additional message
        if probability < 0.30:

            st.success(
                "This customer currently shows a relatively low churn risk."
            )

        elif probability < 0.60:

            st.warning(
                "This customer shows a moderate churn risk and may need attention."
            )

        else:

            st.error(
                "This customer shows a high churn risk and may require retention action."
            )

    except Exception as e:

        st.error(
            "Prediction could not be completed. "
            "Please check that the input values match the training data."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <div>
        Created by
    </div>

    <div class="footer-name">
        Eng. <span>Habiba Ahmed</span>
    </div>

    <div class="footer-project">
        Telco Customer Churn Prediction • Machine Learning
    </div>

</div>
""", unsafe_allow_html=True)
