
import streamlit as st
from datetime import datetime

# Basic Abjad dictionary
abjad_dict = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
    'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
    'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
}

def name_to_abjad(name):
    return sum(abjad_dict.get(char, 0) for char in name if char in abjad_dict)

def suggest_quran_verse(value):
    verse_map = {
        1: "Surah Al-Fatiha:1 - In the name of Allah, the Most Gracious, the Most Merciful.",
        2: "Surah Al-Baqarah:2 - This is the Book about which there is no doubt...",
        3: "Surah Al-Imran:3 - He has sent down upon you the Book in truth...",
    }
    return verse_map.get(value % 3 + 1, "Surah Al-Fatiha:1 - In the name of Allah...")

def wisdom_from_ali():
    return "Patience is of two kinds: patience over what pains you, and patience against what you covet."

st.set_page_config(page_title="Simple Abrahamic Reader", layout="centered")
st.title("🕋 Abrahamic Name Reader (Simplified)")

name = st.text_input("🔤 Your Full Name (in Arabic)")
mother = st.text_input("👩 Mother's Name (in Arabic)")
dob = st.date_input("📅 Your Date of Birth", min_value=datetime(1900, 1, 1), max_value=datetime(2100, 1, 1))

if st.button("🔍 Get Your Reading"):
    if not name or not mother:
        st.error("Please fill in all fields.")
    else:
        total = name_to_abjad(name + mother)
        st.success("✅ Reading Complete")
        st.markdown(f"📊 Abjad Value: `{total}`")
        st.markdown(f"📖 Suggested Verse: {suggest_quran_verse(total)}")
        st.markdown(f"🪶 Wisdom from Imam Ali (ع): *{wisdom_from_ali()}*")
