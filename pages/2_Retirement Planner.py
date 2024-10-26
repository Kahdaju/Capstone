import streamlit as st
import time
import numpy as np
from crewai import Agent, Crew, Process, Task
from crewai_tools import (WebsiteSearchTool, ScrapeWebsiteTool, PDFSearchTool,DOCXSearchTool)
from dotenv import load_dotenv
from openai import OpenAI
import os




st.title("Retirement Planner")
 
with st.form("plan_form"):
    st.subheader("Set your retirement income goal ")
    age = st.slider("How old are you this year?", 20, 65, 25)
    pv = st.slider("How much is your desired monthly payout?", 1000, 500, 5000, step=100)
    

    # Every form must have a submit button.
    submitted = st.form_submit_button("Set Goal")
    
    if submitted:
       st.toast(f"Please give us some time. Retirement planning in progress...")
       # Calculate years until age 65
       years_until_65 = 65 - age
       # Calculate future value using compound interest formula
       future_value = pv * (1 + 0.02) ** years_until_65
    
       # Display the calculated future value
       st.subheader("Retirement goal at 65",divider="green")
       st.subheader(f"Your payout goal in today's dollars : ${pv:,.0f}")
       st.subheader(f"Your payout goal at 65 with inflation of 2% factored in : ${future_value:,.0f}")
       with st.spinner('Taking in your inputs and planning your retirement...'):
        time.sleep(5)
        st.success("The retirement plan will be shown below. Thank you for your patience!")
    else:
        pass
   


#tools

payout=PDFSearchTool(pdf='data/CPF LIFE payout examples 2022.pdf')

retirees=WebsiteSearchTool(pdf='https://www.moneysense.gov.sg/files/Basic%20Financial%20Planning%20Guide/english__pre_retirees.pdf')
planning=WebsiteSearchTool(wurl='https://www.moneysense.gov.sg/legacy-planning/planning-for-retirement/')
retirement_needs=ScrapeWebsiteTool(website_url='https://www.moneysense.gov.sg/legacy-planning/retirement-needs/')

options=ScrapeWebsiteTool(website_url='https://www.moneysense.gov.sg/options-for-your-retirement-income/')

below30 = DOCXSearchTool(docx='data/below30_children.docx')
family_retirees=DOCXSearchTool(docx='data/family_retirees.docx')

# --- Agents ---

# #Agent 1
research = Agent(
    role="Research Agent",
    goal="Research and advice the user based on the {age} and {pv} inputs.",
    allow_delegation=False,
    verbose=True,
    backstory=(
        """
        You are the research expert on retirement planning. 
        """
    ),
 )

#Agent 2 
manager = Agent(
    role="Manager",
    goal="Review and check the advice given by the Research Agent",
    allow_delegation=True,
    verbose=True,
    backstory=(
        """
        You are adept at revising, reviewing and providing financial advice on answers 
        given by the Research agent. You are a professional and an expert in retirement planning.
        """
    ), 
)


# --- Tasks ---
research_task = Task(
     description= (          
         """"
         You are to use the tools given to find the appropriate retirement planning strategies based on
         user input {age}, present value {pv} and retirement income goals. 
         """
    ),

     expected_output=
         """
         A list of practical and sound strategies for the retirement planning. Refer to the tools
         to come up with a plan.
        """
         ,
     tools=[payout,planning,retirement_needs,below30,family_retirees,options],
     agent=research,
 )

#task 2
review_task = Task(
    description= (
        """     
        Review the context you got and expand each topic into a full section for a detailed strategy.
        Make sure the strategy is easy to understand and contains any and all relevant information.
        If possible, show a case study. DO NOT MAKE assumptions and follow strictly from the given tools.
      
        """
    ),
    expected_output=(
        """
        A summary of the strategy with headers and practical information and advice. Include tables, case studies and
        forecasts of different phases in life according to {age} and retirement goals.
                """),       
    
       agent=manager,
)

# # --- Crew ---
crew = Crew(
    agents=[research, manager],
    tasks=[research_task, review_task ],
    full_output=False,
    verbose=0,
    process=Process.sequential,
)


# function
def process_retirement_plan(age,pv):
    delimiter = "```"
    inputs = {
        "age": age,
        "pv": pv
    }
    result = crew.kickoff(inputs=inputs)
    return result

response=process_retirement_plan(age,pv)
st.markdown(response)


   
