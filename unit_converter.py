import streamlit as st # type: ignore

def convert_units(value, unit_from, unit_to):
    
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,

    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        # st.success("Congratulations! You have converted the units successfully!")
        st.success("Congratulations! You have converted the units successfully!", icon="✅")
        st.balloons()
        result = value * conversions[key]
        return    st.write(f"The result is: {result}")


    else:
        return st.write("Conversion not available")
    

st.title("Unit Converter")
value = st.number_input("Enter the Value:", min_value=1.0, step=1.0)
unit_from = st.selectbox("From:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("To:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)