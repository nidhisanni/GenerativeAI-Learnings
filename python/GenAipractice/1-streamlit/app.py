import streamlit as st
 
st.title("Hello Streamlit")
st.header("Welcome to my first Streamlit app!")
st.subheader("This is a subheader")
st.write("This is a simple text display in Streamlit.")

name = st.text_input("Enter your name:")

if name:
    st.write(f"You typed: {name}")  # shows even before clicking

if st.button("Submit"):
    st.success(f"Hello, {name}! Welcome to the app 🎉")
