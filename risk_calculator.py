import streamlit as st

st.set_page_config(page_title="Risk Calculator", layout="centered")

st.title("📈 Risk Calculator – Position Sizing")

st.write("Enter your **current balance** and **risk percentage** to calculate:")
st.write("- Amount to risk (1R)")
st.write("- 2R target")
st.write("- Recommended SL/TP values")

balance = st.number_input("Account Balance ($)", min_value=0.0, step=10.0, format="%.2f")
risk_percent = st.number_input("Risk Percentage (%)", min_value=0.0, step=0.5, format="%.2f")

if risk_percent > 0 and balance > 0:
    risk_amount = balance * (risk_percent / 100)
    tp_2r = risk_amount * 2
    sl_1r = risk_amount

    st.subheader("📊 Results")
    st.metric("Risk Amount (1R)", f"${risk_amount:,.2f}")
    st.metric("Take Profit (2R)", f"${tp_2r:,.2f}")
    st.metric("Stop Loss (1R)", f"${sl_1r:,.2f}")
else:
    st.warning("Please enter both balance and risk % to calculate.")
