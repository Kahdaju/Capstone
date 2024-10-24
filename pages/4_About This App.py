import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="CPF Retirement App - About This App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this App")

st.header("Project Scope")
st.subheader("Empowering Retirement Confidence", divider = "green")
st.write('''At CPFB, we understand that retirement planning can be complex and overwhelming, 
         especially when navigating Singapore's Central Provident Fund (CPF) policies. 
         Central Provident Fund (CPF) policies. Our mission is to provide clarity, guidance, 
         and support to retirees aged 55 and above, empowering them to make informed decisions about their golden years.''')
st.subheader("Objectives", divider = "green")
st.write('''The CPF Retirement App was created to address the growing need for accessible and accurate 
         information on CPF retirement policies. Using AI, configured to be passionate about retirement planning 
         and financial literacy, the app provides personalized answers to frequently asked questions and concerns.
         ''')
st.header("Data Sources", divider = "green")

st.markdown('''
            
The data derived in this site is from:
- The CPF website on  **Retirement Scheme**.
- Moneysense website on  **Planning for Retirement**
- Retirement data   **Data.gov.sg**
            ''')
         
         


with st.expander("Features on This Site"):
    st.subheader("Home-Retirement Query")
    st.write("1. Enter your enquiries in the text box.")
    st.write("3. The app will generate a reply based on your enquiries.")
    st.subheader("Retirement Planner")
    st.write("1. Input your details.")
    st.write("2. Click the 'Set Goal' button.")
    st.write("3. The app will plan a retirement strategy based on your inputs.")
    st.subheader("Statistics on Retirement")
    st.write("This shows information on the total payout disbursed by CPFB through the years.")
   





with st.expander("Disclaimer"):
    st.subheader("IMPORTANT NOTICE") 
    st.write("""
             This web application is a prototype developed for educational purposes only.              
             The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
             Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.
             Always consult with qualified professionals for accurate and personalized advice.
             """)

