import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="CPF Retirement App - About This App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology")

st.subheader("Flowcharts for the CPF Retirement Assistant App and Retirement Planner.")



col1,col2 = st.columns(2)

with col1:
    # st.header("CPF Retirement Query")
    st.image ("images/Query.png", caption="CPF Retirement Query",output_format="png")
with col2:
    # st.header("Retirement Planner")
    st.image ("images/Retirement Planner.png", caption="Retirement Planner",output_format="png")
