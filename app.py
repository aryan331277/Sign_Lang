import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Sign Language Recognition System", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("🖐️ Sign Language Recognition System")
st.markdown("### Select a feature to proceed:")

# Create three columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔤 Sign Language Letter Detection"):
        st.success("Sign Language Letter Detection selected!")
        st.image("https://via.placeholder.com/400", caption="Letter Detection in Action")  # Placeholder image

with col2:
    if st.button("🤟 Gesture Detection"):
        st.success("Gesture Detection selected!")
        st.image("https://via.placeholder.com/400", caption="Gesture Recognition in Action")  # Placeholder image

with col3:
    if st.button("😊 Emotion Detection"):
        st.success("Emotion Detection selected!")
        st.image("https://via.placeholder.com/400", caption="Emotion Analysis in Action")  # Placeholder image

# Footer
st.markdown("---")
