import streamlit as st
from combined import combined_output

# Page config
st.set_page_config(page_title="Healthcare Feedback Analyzer", page_icon="🏥")

# Title
st.title("🏥 Healthcare Feedback Analyzer")

# Description
st.markdown("Analyze hospital feedback and categorize issues automatically.")

# Input box
user_input = st.text_area("📝 Enter feedback:", height=150)

# Button
if st.button("🔍 Analyze Feedback"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some feedback.")
    else:
        final, rule, ml = combined_output(user_input)

        st.markdown("---")

        # Rule-based
        st.subheader("📌 Rule-based Detection")
        if rule:
            st.info(", ".join(rule))
        else:
            st.write("No rule-based match found")

        # ML prediction
        st.subheader("🤖 ML Prediction")
        st.success(ml)

        # Final output
        st.subheader("✅ Final Categories")
        st.success(", ".join(final))