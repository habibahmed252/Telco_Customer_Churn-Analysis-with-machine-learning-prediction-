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
# REFINED DARK / BLUE THEME
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;700&display=swap');


/* ==========================================================
   BASE
========================================================== */

html, body, [class*="css"] {

    font-family: 'Inter', -apple-system, sans-serif;
}


.stApp {

    background:
        radial-gradient(
            circle at 8% 8%,
            rgba(21,151,255,0.10),
            transparent 32%
        ),

        radial-gradient(
            circle at 92% 15%,
            rgba(21,151,255,0.06),
            transparent 32%
        ),

        #05070B;

    color: #E9EFF6;
}


.block-container {

    max-width: 1100px;

    padding-top: 34px;

    padding-bottom: 50px;
}


/* ==========================================================
   HERO
========================================================== */

.hero {

    background: #0A0F17;

    border: 1px solid rgba(21,151,255,.22);

    border-radius: 22px;

    padding: 46px 40px;

    text-align: center;

    margin-bottom: 18px;

    box-shadow: 0 20px 60px rgba(0,0,0,.45);
}


.hero-title {

    font-family: 'Sora', sans-serif;

    font-size: 40px;

    font-weight: 700;

    color: #F5F8FC;

    letter-spacing: -0.5px;
}


.hero-title span {

    color: #1597FF;
}


.hero-text {

    font-family: 'Inter', sans-serif;

    color: #8FA0B5;

    font-size: 16px;

    line-height: 1.75;

    margin-top: 14px;

    max-width: 560px;

    margin-left: auto;

    margin-right: auto;
}


/* ==========================================================
   CREATED BY — name lives right below the hero now
========================================================== */

.created-by {

    text-align: center;

    font-family: 'Inter', sans-serif;

    font-size: 14px;

    color: #6E7C8C;

    margin-bottom: 38px;
}


.created-by span {

    font-family: 'Sora', sans-serif;

    font-weight: 600;

    color: #1597FF;
}


/* ==========================================================
   SECTION
========================================================== */

.section-title {

    font-family: 'Sora', sans-serif;

    font-size: 21px;

    font-weight: 600;

    color: #F5F8FC;

    margin-top: 8px;
}


.section-line {

    width: 48px;

    height: 3px;

    background: #1597FF;

    border-radius: 4px;

    margin-top: 10px;

    margin-bottom: 26px;

    opacity: .85;
}


.group-label {

    font-family: 'Sora', sans-serif;

    font-size: 14px;

    font-weight: 600;

    color: #1597FF;

    margin-bottom: 4px;
}


/* ==========================================================
   INPUTS
========================================================== */

div[data-baseweb="select"] > div {

    background-color: #0B1119 !important;

    border: 1px solid #202B38 !important;

    border-radius: 10px !important;

    color: #E9EFF6 !important;
}


div[data-baseweb="select"] > div:hover {

    border-color: #1597FF !important;
}


.stNumberInput input {

    background: #0B1119 !important;

    color: #E9EFF6 !important;

    border: 1px solid #202B38 !important;

    border-radius: 10px !important;
}


label {

    font-family: 'Inter', sans-serif;

    color: #B7C3D1 !important;

    font-weight: 500 !important;

    font-size: 14px !important;
}


/* ==========================================================
   EXPANDER (Optional section)
========================================================== */

.streamlit-expanderHeader {

    font-family: 'Sora', sans-serif !important;

    font-size: 14px !important;

    font-weight: 600 !important;

    color: #6E7C8C !important;

    background: #0A0F17 !important;

    border: 1px solid #171F29 !important;

    border-radius: 12px !important;
}


.streamlit-expanderContent {

    background: #070B11 !important;

    border: 1px solid #171F29 !important;

    border-top: none !important;

    border-radius: 0 0 12px 12px !important;
}


/* ==========================================================
   BUTTON
========================================================== */

div.stButton > button {

    width: 100%;

    height: 56px;

    border-radius: 12px;

    background: linear-gradient(90deg, #0A6FE0, #1597FF);

    color: white;

    border: none;

    font-family: 'Sora', sans-serif;

    font-size: 17px;

    font-weight: 600;

    box-shadow: 0 12px 28px rgba(21,151,255,.22);

    transition: transform .15s ease, box-shadow .15s ease;
}


div.stButton > button:hover {

    transform: translateY(-1px);

    box-shadow: 0 16px 34px rgba(21,151,255,.32);
}


/* ==========================================================
   RESULT
========================================================== */

.result-card {

    background: #0A0F17;

    border: 1px solid rgba(21,151,255,.28);

    border-radius: 22px;

    padding: 44px 30px;

    text-align: center;

    margin-top: 36px;

    box-shadow: 0 20px 60px rgba(0,0,0,.45);
}


.result-title {

    font-family: 'Sora', sans-serif;

    font-size: 20px;

    font-weight: 600;

    color: #B7C3D1;

    margin-bottom: 22px;
}


.result-message {

    font-family: 'Inter', sans-serif;

    font-size: 14px;

    color: #6E7C8C;

    margin-top: 22px;

    max-width: 420px;

    margin-left: auto;

    margin-right: auto;

    line-height: 1.6;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {

    text-align: center;

    margin-top: 56px;

    padding-top: 22px;

    border-top: 1px solid #171F29;

    color: #4A5563;

    font-family: 'Inter', sans-serif;

    font-size: 13px;
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
# HERO
# ============================================================

st.markdown(
    '<div class="hero">'
    '<div class="hero-title">Telco Customer <span>Churn AI</span></div>'
    '<div class="hero-text">'
    'Intelligent customer churn prediction powered by Machine Learning and XGBoost. '
    'Analyze customer behavior and estimate the probability of customer churn.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CREATED BY — right below the hero box
# ============================================================

st.markdown(
    '<div class="created-by">Created by <span>Eng. Habiba Ahmed Talat</span></div>',
    unsafe_allow_html=True
)


# ============================================================
# CUSTOMER INFORMATION — core, high-impact fields only
# ============================================================

st.markdown(
    '<div class="section-title">Please enter your information</div>'
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMN 1 — Tenure & Contract
# ============================================================

with col1:

    st.markdown(
        '<div class="group-label">Tenure &amp; Contract</div>',
        unsafe_allow_html=True
    )

    tenure = st.number_input(
        "Tenure (months with the company)",

        min_value=0,

        max_value=72,

        value=12,

        step=1
    )


    contract = st.selectbox(
        "Contract",

        [
            "Month-to-month",
            "One year",
            "Two year"
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


# ============================================================
# COLUMN 2 — Charges
# ============================================================

with col2:

    st.markdown(
        '<div class="group-label">Charges</div>',
        unsafe_allow_html=True
    )

    monthly = st.number_input(
        "Monthly Charges",

        min_value=0.0,

        max_value=20000.0,

        value=70.0,

        step=1.0
    )


    total = st.number_input(
        "Total Charges (lifetime spend)",

        min_value=0.0,

        max_value=50000.0,

        value=1000.0,

        step=10.0
    )


# ============================================================
# COLUMN 3 — Service Information
# ============================================================

with col3:

    st.markdown(
        '<div class="group-label">Please enter service information</div>',
        unsafe_allow_html=True
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


    tech_support = st.selectbox(
        "Tech Support Service",

        [
            "HasTech Support",
            "No Tech Support",
            "No Internet Service"
        ]
    )


# ============================================================
# OPTIONAL DETAILS — lower-impact fields, collapsed by default
# ============================================================

st.write("")

with st.expander("Optional details"):

    ocol1, ocol2, ocol3, ocol4 = st.columns(4)

    with ocol1:

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

    with ocol2:

        dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

        phone = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",

            [
                "Yes",
                "No",
                "No phone service"
            ]
        )

    with ocol3:

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

        paperless = st.selectbox(
            "Paperless Billing",

            [
                "Yes",
                "No"
            ]
        )

    with ocol4:

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
        # RISK + COLOR (blue = fine, red = risky)
        # ====================================================

        if probability < 0.30:

            risk = "Low Risk"

            ring_color = "#1597FF"

            message = (
                "This customer currently shows "
                "a relatively low churn risk."
            )

        elif probability < 0.60:

            risk = "Medium Risk"

            ring_color = "#1597FF"

            message = (
                "This customer shows a moderate "
                "churn risk and may need attention."
            )

        else:

            risk = "High Risk"

            ring_color = "#FF4D6A"

            message = (
                "This customer shows a high churn "
                "risk and may require retention action."
            )


        # ====================================================
        # CIRCULAR GAUGE (SVG ring, fills with risk color)
        # ====================================================

        radius = 80
        stroke_width = 14
        circumference = 2 * 3.14159265 * radius
        filled = circumference * probability
        offset = circumference - filled

        gauge_svg = f'''
        <svg width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="{radius}" fill="none" stroke="#141B24" stroke-width="{stroke_width}"></circle>
            <circle cx="100" cy="100" r="{radius}" fill="none" stroke="{ring_color}" stroke-width="{stroke_width}" stroke-linecap="round" stroke-dasharray="{circumference:.2f}" stroke-dashoffset="{offset:.2f}" transform="rotate(-90 100 100)"></circle>
            <text x="100" y="94" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="34" font-weight="700" fill="#F5F8FC">{percentage:.1f}%</text>
            <text x="100" y="120" text-anchor="middle" font-family="Sora, sans-serif" font-size="14" font-weight="600" fill="{ring_color}">{risk}</text>
        </svg>
        '''

        st.markdown(
            '<div class="result-card">'
            '<div class="result-title">Prediction Result</div>'
            f'{gauge_svg}'
            f'<div class="result-message">{message}</div>'
            '</div>',
            unsafe_allow_html=True
        )


    except Exception as e:

        st.error(
            "Prediction failed."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    'Telco Customer Churn Prediction • Machine Learning • XGBoost'
    '</div>',
    unsafe_allow_html=True
)
