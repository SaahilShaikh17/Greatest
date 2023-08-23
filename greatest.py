import streamlit as st

st.set_page_config(page_title="Muskan's greatest of 3")

st.title("Finding the greatest number out of 3 given values")
st.subheader("This app compares the inputs and outputs the biggest number")

num1 = st.number_input('Insert the first number')
num2 = st.number_input('Insert the second number')
num3 = st.number_input('Insert the third number')

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
  
st.write('The largest is ', largest)
