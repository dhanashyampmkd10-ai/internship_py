import streamlit as st

st.title("Greeting App")

# Initialize session state
if "name" not in st.session_state:
    st.session_state.name = ""

name = st.text_input("Enter your name")

if st.button("Greet"):
    st.session_state.name = name

if st.session_state.name:
    st.success(f"Hello, {st.session_state.name}!")