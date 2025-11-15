import streamlit as st

st.set_page_config(page_title="Risk Calculator & Plan", layout="centered")

st.title("📈 Risk Calculator & Compounding Plan")

# Tabs for cleaner layout
tab_calc, tab_summary = st.tabs(["💰 Risk Calculator", "📜 Risk Approach Summary"])

with tab_calc:
    st.header("💰 Position Sizing – Risk Calculator")

    st.write(
        "Enter your **current balance** and **risk percentage** to calculate:\n"
        "- Amount to risk (**1R**)\n"
        "- **2R** profit target\n"
        "- Helps you stay aligned with your compounding plan"
    )

    balance = st.number_input(
        "Account Balance ($)", min_value=0.0, step=10.0, format="%.2f"
    )
    risk_percent = st.number_input(
        "Risk Percentage (%)", min_value=0.0, step=0.5, format="%.2f"
    )

    if risk_percent > 0 and balance > 0:
        risk_amount = balance * (risk_percent / 100)   # 1R
        tp_2r = risk_amount * 2                        # 2R
        sl_1r = risk_amount                            # 1R

        st.subheader("📊 Results")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Risk Amount (1R)", f"${risk_amount:,.2f}")
        with col2:
            st.metric("Take Profit (2R)", f"${tp_2r:,.2f}")
        with col3:
            st.metric("Stop Loss (1R)", f"${sl_1r:,.2f}")

        st.caption(
            "✅ Make sure this risk % matches your current phase "
            "in the compounding plan."
        )
    else:
        st.warning("Enter both **balance** and **risk %** to calculate.")

with tab_summary:
    st.header("📜 My Risk Approach – $100 → $1,000,000")

    st.markdown(
        """
### 🌍 Overview

You follow a **3-phase compounding framework**:

- Use **higher risk** when the account is small and recoverable  
- Gradually **reduce risk** as capital grows and must be protected  
- Always trade **1:2 R:R**, with **1–3 trades per day** and strict discipline  

---

### 🔵 Phase 1 – Full Kelly (High Risk)

**Balance range:** **$100 → $10,000**  
**Risk per trade:** **10–25%**  
**Goal:** Explosive growth from a small account  

**Sub-stages:**
- `$100 → $300` → Risk **10–12%**
- `$300 → $1,000` → Risk **12–18%**
- `$1,000 → $10,000` → Risk **20–25%**

**Approx:**
- **Trades:** ~40–90  
- **Time:** ~1–2.5 months (with 1–3 trades/day)

---

### 🟠 Phase 2 – Aggressive (½ Kelly)

**Balance range:** **$10,000 → $100,000**  
**Risk per trade:** **8–16%**  
**Goal:** Fast but controlled growth  

**Sub-stages:**
- `$10,000 → $30,000` → Risk **12–16%**
- `$30,000 → $60,000` → Risk **10–12%**
- `$60,000 → $100,000` → Risk **8–10%**

**Approx:**
- **Trades:** ~30–70  
- **Time:** ~1–2 months  

---

### 🟢 Phase 3 – Original (¼ Kelly)

**Balance range:** **$100,000 → $1,000,000**  
**Risk per trade:** **2–6%**  
**Goal:** Capital preservation + smooth compounding  

**Sub-stages:**
- `$100,000 → $250,000` → Risk **4–6%**
- `$250,000 → $500,000` → Risk **3–4%**
- `$500,000 → $1,000,000` → Risk **2–3%**

**Approx:**
- **Trades:** ~120–250  
- **Time:** ~3–7 months  

---

### 📆 Big Picture – Time & Trades

- **Total trades:** ~**190–410**  
- **Fast timeline:** **5–6 months**  
- **Normal timeline:** **7–11 months**  
- **Extended with mistakes:** **12–18 months**

---

### 🧠 Core Rules of the Path

- I trade **only 1:2 R:R setups**  
- I take **1–3 trades per day** maximum  
- I **STOP after 2 consecutive losses** or emotional tilt  
- I **never increase risk after a loss**  
- I **always calculate risk % based on my current phase**  
- I protect capital first, grow second  
- I am building **$100 → $1,000,000** through discipline and consistency  

---
"""
    )

    with st.expander("💡 How to Use This Summary"):
        st.markdown(
            """
- Use the **Risk Calculator** tab before every trade  
- Make sure your **risk % matches your current phase**  
- Re-read this summary every session to stay aligned with the big picture  
- Treat these rules as **non-negotiable** – the edge is in execution, not prediction  
"""
        )
