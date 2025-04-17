import streamlit as st
import re

def check_password_strength(password):
    length = len(password) >= 8
    lowercase = re.search(r"[a-z]", password)
    uppercase = re.search(r"[A-Z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, bool(lowercase), bool(uppercase), bool(digit), bool(special)])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its strength:")

password = st.text_input("Password", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"**Password Strength:** {strength}")
