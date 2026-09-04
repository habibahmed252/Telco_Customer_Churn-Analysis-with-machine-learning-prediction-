import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Telco Churn AI",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# DARK BLACK / WHITE / BLUE DESIGN
# ============================================================

st.markdown("""
<style>

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0, 119, 255, 0.12),
            transparent 30%
        ),

        radial-gradient(
            circle at 90% 20%,
            rgba(0, 119, 255, 0.08),
            transparent 30%
        ),

        #05070B;

    color: white;
}


.block-container {

    max-width: 1150px;

    padding-top: 35px;

    padding-bottom: 40px;
}


/* ==========================================================
   HERO
========================================================== */

.hero {

    background:
        linear-gradient(
            145deg,
            #0D1520,
            #070B11
        );

    border:
        1px solid
        rgba(21,151,255,.35);

    border-radius: 25px;

    padding: 45px 30px;

    text-align: center;

    margin-bottom: 35px;

    box-shadow:
        0 15px 50px
        rgba(0,0,0,.5),

        0 0 40px
        rgba(0,119,255,.08);
}


.hero-title {

    font-size: 46px;

    font-weight: 900;

    color: white;
}


.hero-title span {

    color: #1597FF;
}


.hero-text {

    color: #AAB6C5;

    font-size: 17px;

    line-height: 1.7;

    margin-top: 12px;
}


/* ==========================================================
   SECTION
========================================================== */

.section-title {

    font-size: 25px;

    font-weight: 850;

    color: white;

    margin-top: 20px;
}


.section-line {

    width: 65px;

    height: 3px;

    background: #1597FF;

    border-radius: 5px;

    margin-top: 8px;

    margin-bottom: 25px;
}


/* ==========================================================
   INPUTS
========================================================== */

div[data-baseweb="select"] > div {

    background-color:
        #0B1119 !important;

    border:
        1px solid
        #273444 !important;

    border-radius:
        11px !important;

    color:
        white !important;
}


div[data-baseweb="select"] > div:hover {

    border-color:
        #1597FF !important;
}


.stNumberInput input {

    background:
        #0B1119 !important;

    color:
        white !important;

    border:
        1px solid
        #273444 !important;

    border-radius:
        11px !important;
}


label {

    color:
        #DCE5EE !important;

    font-weight:
        600 !important;
}


/* ==========================================================
   BUTTON
========================================================== */

div.stButton > button {

    width: 100%;

    height: 60px;

    border-radius: 14px;

    background:
        linear-gradient(
            90deg,
            #006FFF,
            #159FFF
        );

    color: white;

    border: none;

    font-size: 19px;

    font-weight: 800;

    box-shadow:
        0 10px 30px
        rgba(0,119,255,.25);

    transition: .2s;
}


div.stButton > button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 15px 35px
        rgba(0,119,255,.4);
}


/* ==========================================================
   RESULT
========================================================== */

.result-card {

    background:
        linear-gradient(
            145deg,
            #0D1622,
            #070B11
        );

    border:
        1px solid
        rgba(21,151,255,.45);

    border-radius: 25px;

    padding: 40px 25px;

    text-align: center;

    margin-top: 35px;

    box-shadow:
        0 15px 50px
        rgba(0,0,0,.5);
}


.result-title {

    font-size: 28px;

    font-weight: 800;

    color: white;
}


.probability {

    font-size: 58px;

    font-weight: 900;

    color: #1597FF;

    margin-top: 12px;
}


.probability-label {

    color: #8F9DAD;

    font-size: 15px;
}


.risk {

    font-size: 25px;

    font-weight: 800;

    color: white;

    margin-top: 20px;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {

    text-align: center;

    margin-top: 60px;

    padding-top: 25px;

    border-top:
        1px solid
        #202B38;

    color: #778494;

    font-size: 15px;
}


.footer-created {

    font-size: 15px;

    color: #8996A5;
}


.footer-name {

    font-size: 24px;

    font-weight: 900;

    color: white;

    margin-top: 7px;
}


.footer-name span {

    color: #1597FF;
}


.footer-project {

    margin-top: 8px;

    font-size: 13px;

    color: #5E6B7A;
}


/* ==========================================================
   PROGRESS
========================================================== */

div[data-testid="stProgress"] > div > div {

    background-color:
        #1597FF !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load(
        "telco_churn_model.pkl"
    )


try:

    model = load_model()

except Exception as e:

    st.error(
        "The trained model could not be loaded."
    )

    st.exception(e)

    st.stop()


# ============================================================
# HEADER  (FIXED: single line, no indentation/blank lines)
# ============================================================

st.markdown(
    '<div class="hero">'
    '<div class="hero-title">Telco Customer <span>Churn AI</span></div>'
    '<div class="hero-text">'
    'Intelligent customer churn prediction powered by Machine Learning and XGBoost.'
    '<br><br>'
    'Analyze customer behavior and estimate the probability of customer churn.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CUSTOMER INFORMATION  (FIXED)
# ============================================================

st.markdown(
    '<div class="section-title">Customer Information</div>'
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMN 1
# ============================================================

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )


    senior = st.selectbox(
        "Senior Citizen",
        [0, 1],

        format_func=lambda x:
            "Yes" if x == 1 else "No"
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


# ============================================================
# COLUMN 2
# ============================================================

with col2:

    multiple_lines = st.selectbox(
        "Multiple Lines",

        [
            "Yes",
            "No",
            "No phone service"
        ]
    )


    internet = st.selectbox(
        "Internet Service",

        [
            "DSL",
            "Fiber optic",
            "No"
        ]
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


# ============================================================
# COLUMN 3
# ============================================================

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

        [
            "Yes",
            "No"
        ]
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
# ANALYZE
# ============================================================

st.write("")


if st.button("Analyze Customer"):

    try:

        customer = pd.DataFrame([{

            "gender":
                gender,

            "SeniorCitizen statue":
                senior,

            "Dependents":
                dependents,

            "Partner":
                partner,

            "Phone Service":
                phone,

            "tenure":
                tenure,

            "Having Multiple Lines":
                multiple_lines,

            "InternetService":
                internet,

            "Online Security":
                online_security,

            "OnlineBackup":
                online_backup,

            "DeviceProtection":
                device_protection,

            "Tech Support Service":
                tech_support,

            "Streaming TV Service":
                streaming_tv,

            "Streaming Movies Service":
                streaming_movies,

            "Contract":
                contract,

            "PaperlessBilling":
                paperless,

            "PaymentMethod":
                payment,

            "MonthlyCharges":
                monthly,

            "TotalCharges":
                total
        }])


        # ====================================================
        # ENSURE EXACT TRAINING COLUMN ORDER
        # ====================================================

        customer = customer[
            model.feature_names_in_
        ]


        # ====================================================
        # PREDICTION
        # ====================================================

        probability = model.predict_proba(
            customer
        )[0][1]


        percentage = probability * 100


        # ====================================================
        # RISK
        # ====================================================

        if probability < 0.30:

            risk = "LOW RISK"

            message = (
                "This customer currently shows "
                "a relatively low churn risk."
            )

        elif probability < 0.60:

            risk = "MEDIUM RISK"

            message = (
                "This customer shows a moderate "
                "churn risk and may need attention."
            )

        else:

            risk = "HIGH RISK"

            message = (
                "This customer shows a high churn "
                "risk and may require retention action."
            )


        # ====================================================
        # RESULT  (FIXED: single line, no indentation/blank lines)
        # ====================================================

        st.markdown(
            '<div class="result-card">'
            '<div class="result-title">Prediction Result</div>'
            f'<div class="probability">{percentage:.1f}%</div>'
            '<div class="probability-label">Estimated Customer Churn Probability</div>'
            f'<div class="risk">{risk}</div>'
            '</div>',
            unsafe_allow_html=True
        )


        st.write("")


        st.progress(
            float(probability)
        )


        if probability < 0.30:

            st.success(message)

        elif probability < 0.60:

            st.warning(message)

        else:

            st.error(message)


    except Exception as e:

        st.error(
            "Prediction failed."
        )

        st.exception(e)


# ============================================================
# FOOTER  (FIXED: single line, no indentation/blank lines)
# ============================================================

st.markdown(
    '<div class="footer">'
    '<div class="footer-created">Created by</div>'
    '<div class="footer-name">Eng. <span>Habiba Ahmed</span></div>'
    '<div class="footer-project">'
    'Telco Customer Churn Prediction • Machine Learning • XGBoost'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)
