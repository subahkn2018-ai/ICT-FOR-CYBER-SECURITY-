import streamlit as st
import pandas as pd

st.set_page_config(page_title="Industrial IoT Security Audit Tool", page_icon="🔒")

# Team Members
st.title("🔒 Industrial IoT Security Audit Tool")

st.markdown("""
### Group Members
- Saif Ali
- Maaz Ahmad
- Abdullah Hameed
- Muhammad Mudasir
""")

st.write("This tool performs a basic Industrial IoT Cyber Security Audit based on common security controls.")

st.header("Security Audit Checklist")

questions = {
    "Are default passwords changed on all devices?": 10,
    "Is multi-factor authentication enabled?": 10,
    "Are software and firmware updates regularly installed?": 10,
    "Is network traffic encrypted?": 10,
    "Are firewalls configured properly?": 10,
    "Is access control implemented?": 10,
    "Are security logs monitored regularly?": 10,
    "Is backup and recovery plan available?": 10,
    "Are IoT devices segmented from the main network?": 10,
    "Is employee cyber security training conducted?": 10
}

score = 0

responses = {}

for question, marks in questions.items():
    response = st.radio(
        question,
        ["Yes", "No"],
        key=question
    )
    responses[question] = response

    if response == "Yes":
        score += marks

if st.button("Generate Audit Report"):

    st.subheader("Audit Results")

    df = pd.DataFrame(
        {
            "Security Check": responses.keys(),
            "Response": responses.values()
        }
    )

    st.dataframe(df, use_container_width=True)

    st.write(f"### Security Score: {score}/100")

    if score >= 80:
        st.success("Excellent Security Posture ✅")
    elif score >= 60:
        st.warning("Moderate Security Risk ⚠️")
    else:
        st.error("High Security Risk ❌")

    st.subheader("Recommendations")

    for question, response in responses.items():
        if response == "No":
            st.write(f"• Improve: {question}")

st.markdown("---")
st.caption("Industrial IoT Security Audit Tool | ICT Cyber Security Project")
