import streamlit as st  # Import Streamlit for creating the web-based UI


# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function (e.g., temperature conversion), call it
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Otherwise, multiply by the conversion factor
    else:
        return "Conversion not supported"  # Return message if conversion is not defined
# Streamlit UI setup
st.set_page_config(page_title="Unit Converter", page_icon="🌍", layout="centered")  # Set title for the web app

st.markdown(
    """
    <h1 style='text-align: center;'>🌍 Unit Converter</h1>
    <h3 style='text-align: center; color: grey;'>Convert meters, kilometers, grams and kilograms </h3>
    <p style='text-align: center;'>Select a category, enter a value, and see the conversion in real-time!</p>
    """, unsafe_allow_html=True
)

# Streamlit UI setup
st.title(" Unit Converter")  # Set title for the web app

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms"]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    st.write(f"Converted Value: {result}")  # Display the result

# Footer
st.markdown("<br><hr><p style='text-align: center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
