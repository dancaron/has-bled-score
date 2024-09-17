import streamlit as st

# Function to calculate HAS-BLED score
def calculate_has_bled_score(hypertension, renal_disease, liver_disease, stroke_history, bleeding_history, inr_labile, age_65, drugs_alcohol):
    score = sum([hypertension, renal_disease, liver_disease, stroke_history, bleeding_history, inr_labile, age_65, drugs_alcohol])
    return score

# App description
st.title("HAS-BLED Score Calculator")
st.write("""
This app calculates the HAS-BLED score, which estimates the 1-year risk of major bleeding in patients with atrial fibrillation, especially those on anticoagulation therapy. The score is based on several clinical parameters, and a higher score indicates a greater risk of bleeding.
""")

# Input fields
st.sidebar.header("Patient Information")
hypertension = st.sidebar.checkbox("Hypertension (uncontrolled >160mmHg)")
renal_disease = st.sidebar.checkbox("Renal disease (dialysis, transplant, or Cr >200)")
liver_disease = st.sidebar.checkbox("Liver disease (cirrhosis, bilirubin >2x normal, etc.)")
stroke_history = st.sidebar.checkbox("Previous stroke history")
bleeding_history = st.sidebar.checkbox("Bleeding history or predisposition")
inr_labile = st.sidebar.checkbox("Labile INR (unstable/high INR or in range <60% of time)")
age_65 = st.sidebar.checkbox("Age ≥ 65 years")
drugs_alcohol = st.sidebar.checkbox("Concurrent drugs/alcohol usage (antiplatelets, NSAIDs, ≥8 drinks/week)")

# Calculate HAS-BLED score
has_bled_score = calculate_has_bled_score(hypertension, renal_disease, liver_disease, stroke_history, bleeding_history, inr_labile, age_65, drugs_alcohol)

# Display results
st.subheader("HAS-BLED Score")
st.write(f"The HAS-BLED score is: **{has_bled_score}**")

# Risk interpretation
if has_bled_score >= 3:
    st.warning("High risk of bleeding. Consider caution and regular monitoring.")
else:
    st.success("Low to moderate risk of bleeding.")
