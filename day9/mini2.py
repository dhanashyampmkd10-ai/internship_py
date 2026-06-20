import streamlit as st

st.title("Counter App")

# Initialize counter in session_state
if "count" not in st.session_state:
    st.session_state.count = 0

# Increment counter when button is clicked
if st.button("Increment"):
    st.session_state.count += 1

# Display count
st.metric(label="Current Count", value=st.session_state.count)