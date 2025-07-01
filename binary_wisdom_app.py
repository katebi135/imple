
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Binary Wisdom App", layout="centered")

st.title("🧠 Binary Wisdom - Abrahamic Esoteric Portal")
st.markdown("Enter your full details for a multilayered esoteric reading.")

# Helper for Abjad
def abjad_value(text):
    abjad_table = {
        'ا':1, 'ب':2, 'ج':3, 'د':4, 'ه':5, 'و':6, 'ز':7, 'ح':8, 'ط':9,
        'ی':10, 'ك':20, 'ل':30, 'م':40, 'ن':50, 'س':60, 'ع':70, 'ف':80, 'ص':90,
        'ق':100, 'ر':200, 'ش':300, 'ت':400, 'ث':500, 'خ':600, 'ذ':700, 'ض':800,
        'ظ':900, 'غ':1000
    }
    return sum(abjad_table.get(ch, 0) for ch in text if ch in abjad_table)

# Moon Phase logic (placeholder)
def moon_phase(day):
    phases = ['New Moon', 'Waxing Crescent', 'First Quarter', 'Waxing Gibbous',
              'Full Moon', 'Waning Gibbous', 'Last Quarter', 'Waning Crescent']
    return phases[day % 8]

# Simiyā logic (placeholder)
def simiya_analysis(name):
    return f"Simiyā indicates inner harmony and subtle light in {name}."

# Līmiyā logic (placeholder)
def limiya_analysis(name):
    return f"Līmiyā marks transformational potential latent in {name}."

# Jafr logic (placeholder)
def jafr_analysis(name):
    total = abjad_value(name)
    red = total % 9
    white = total % 4
    return f"Jafr values → Red Square: {red}, White Square: {white}"

with st.form("wisdom_form"):
    name = st.text_input("🧍 Full Name")
    dob = st.date_input("📅 Date of Birth", min_value=date(1924,1,1), max_value=date.today())
    mother_name = st.text_input("👩 Mother's Name")
    mother_dob = st.date_input("📅 Mother's Date of Birth", min_value=date(1924,1,1), max_value=date.today())
    father_name = st.text_input("👨 Father's Name")
    father_dob = st.date_input("📅 Father's Date of Birth", min_value=date(1924,1,1), max_value=date.today())

    st.markdown("👶 **Children Information**")
    num_kids = st.slider("Number of Children", 0, 5, 0)
    children = []
    for i in range(num_kids):
        child_name = st.text_input(f"Child {i+1} Name", key=f"child_name_{i}")
        child_dob = st.date_input(f"Child {i+1} DOB", min_value=date(1924,1,1), max_value=date.today(), key=f"child_dob_{i}")
        children.append((child_name, child_dob))

    submitted = st.form_submit_button("🔮 Reveal Wisdom")

if submitted:
    st.subheader("🔍 Esoteric Report")
    st.write(jafr_analysis(name))
    st.write(simiya_analysis(name))
    st.write(limiya_analysis(name))
    st.write(f"🌙 Moon Phase on DOB: {moon_phase(dob.day)}")
    st.write(f"📊 Abjad Value of Name: {abjad_value(name)}")

    st.markdown("📚 *For entertainment and educational purposes only*")
