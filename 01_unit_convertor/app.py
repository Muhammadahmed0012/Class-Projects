import streamlit as st

st.title("Simple Unit Converter")

# Select conversion type
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

# Units list for each type
units = {
    "Length": ["Meter", "Kilometer", "Mile"],
    "Weight": ["Kilogram", "Gram", "Pound"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From unit", units[conversion_type])
to_unit = st.selectbox("To unit", units[conversion_type])

value = st.number_input("Enter value", format="%.2f")


# Conversion functions
def convert_length(value, from_unit, to_unit):
    factor = {
        "Meter": 1,
        "Kilometer": 1000,
        "Mile": 1609.34
    }
    return value * factor[from_unit] / factor[to_unit]

def convert_weight(value, from_unit, to_unit):
    factor = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592
    }
    return value * factor[from_unit] / factor[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Show result
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    st.write(f"Result: {round(result, 2)} {to_unit}")
