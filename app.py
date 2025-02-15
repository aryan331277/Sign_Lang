import streamlit as st

st.title("Sign Language Recognition System")

# Creating three buttons
if st.button("Sign Language Letter Detection"):
    st.write("Sign Language Letter Detection selected!")

if st.button("Gesture Detection"):
    st.write("Gesture Detection selected!")

if st.button("Emotion Detection"):
    st.write("Emotion Detection selected!")
