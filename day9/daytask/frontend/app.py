import streamlit as st
import requests

REGISTER_URL = "http://127.0.0.1:8000/auth/register"
LOGIN_URL = "http://127.0.0.1:8000/auth/login"


# Session state
if "token" not in st.session_state:
    st.session_state.token = None

if "email" not in st.session_state:
    st.session_state.email = None


# Dashboard
if st.session_state.token:

    st.title("Dashboard")

    st.success(f"Welcome, {st.session_state.email}")

    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()


else:

    page = st.sidebar.selectbox(
        "Choose",
        ["Register", "Login"]
    )

    # REGISTER
    if page == "Register":

        st.title("Register")

        with st.form("register_form"):

            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            submit = st.form_submit_button("Register")

        if submit:

            response = requests.post(
                REGISTER_URL,
                json={
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:
                st.success("Registration successful")

            else:
                st.error(response.json()["detail"])

    # LOGIN
    else:

        st.title("Login")

        with st.form("login_form"):

            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            submit = st.form_submit_button("Login")

        if submit:

            response = requests.post(
                LOGIN_URL,
                json={
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.token = data["access_token"]
                st.session_state.email = email

                st.rerun()

            else:
                st.error(response.json()["detail"])