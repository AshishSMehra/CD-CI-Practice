import streamlit as st 

st.title("Power Calculator")
st.write("Enter the to calculate")


n = st.number_input("Enter the number", value=1, step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5


st.write(square)
st.write(cube)
st.write(fifth_power)


