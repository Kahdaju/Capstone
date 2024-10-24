import streamlit as st
import pandas as pd
import numpy as np




retirement_scheme = pd.read_csv('data\Yearly Retirement Scheme.csv')
retirement_scheme['Year'] = retirement_scheme['Year'].astype(str)

cpf_life_scheme=pd.read_csv('data/Yearly CPF LIFE Scheme.csv')
cpf_life_scheme['Year'] = cpf_life_scheme['Year'].astype(str)

above_55_scheme=pd.read_csv('data\Yearly Withdrawal Above 55.csv')
above_55_scheme['Year'] = above_55_scheme['Year'].astype(str)



def retirement(dataframe):
    st.subheader("Yearly Amount of Payout under Retirement Scheme")
    st.write("Figures are rounded to the nearest hundred thousand dollars.")
    st.divider()
    st.dataframe(retirement_scheme)
    st.line_chart(data=retirement_scheme, x='Year',
                   y='Yearly_Payout_Amount', 
                   x_label='Year', 
                  y_label='Total Amount Disbursed')


def cpf_life(dataframe):
    st.subheader("Yearly Amount of Payout under CPF Life Scheme")
    st.write ("""CPF LIFE was established in Sep 2009 and in 2013,
              members began to be auto-included into CPF LIFE, if they meet the qualifying criteria at age 55. 
              From Q3 2015, members who turned 55 from Jul 2015 will
               only be assessed for auto-inclusion six months before their payout eligibility age.
              Figures are rounded to the nearest hundred thousand dollars.""")
    st.divider()
    st.dataframe(cpf_life_scheme)
    st.line_chart(data=cpf_life_scheme, x='Year',
                   y='CPF Life Paid Yearly', 
                   x_label='Year', 
                  y_label='Total Amount Disbursed')

def above_55(dataframe):
    st.subheader("Yearly Withdrawal For Those 55 and above")
    st.write ("""Refers to the withdrawals made by members who reached the age of 55 and have set aside their cohort FRS in their RA. CPF members who are unable to set aside their cohort FRS or at least cohort BRS with a property, can still withdraw up to $5,000 of their savings.
    
Figures are rounded to the nearest hundred thousand dollars..""")
    st.divider()
    st.dataframe(above_55_scheme)
    st.line_chart(data=above_55_scheme, x='Year',
                   y='Yearly Amount for 55 and above', 
                   x_label='Year', 
                  y_label='Total Amount Disbursed')


# Sidebar setup

#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select the information you want to display:', 
                           ['Yearly Amount of Payout under Retirement Scheme', 
                            'Yearly Amount of Payout under CPF Life Scheme', 
                            'Yearly Withdrawal For Those 55 and above'
                            ])



if options == 'Yearly Amount of Payout under Retirement Scheme':
    retirement(retirement_scheme)
elif options == 'Yearly Amount of Payout under CPF Life Scheme':
    cpf_life(cpf_life_scheme)
elif options == 'Yearly Withdrawal For Those 55 and above':
    above_55(above_55_scheme)




