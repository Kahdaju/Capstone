# Set up and run this Streamlit App
import streamlit as st
import hmac
import pandas as pd
# from helper_functions import utility
# from helper_functions.utility import check_password  
from crew1.customer_agent_crew import process_user_message

#  <--------- Check Password Configuration --------->
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

#  <--------- end --------->



# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Home-CPF Retirement App"
)
# endregion <--------- Streamlit App Configuration --------->



st.title("CPF Retirement Assistance App")

form = st.form(key="form")
form.subheader("How can we help you today?")

user_prompt = form.text_area("Enter your queries into the box below", height=100)

if form.form_submit_button("Submit"):
    
    st.toast(f"Let me find out for you on your enquiry - {user_prompt}")

    st.divider()

    response = process_user_message(user_prompt)
   
    st.markdown(response)

