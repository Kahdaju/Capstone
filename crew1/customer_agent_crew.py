from crewai import Agent, Crew, Process, Task
from crewai_tools import (ScrapeWebsiteTool, PDFSearchTool)
from dotenv import load_dotenv
from openai import OpenAI
import os
import streamlit as st
from IPython.display import Markdown


#api keys
if load_dotenv('.env'):
   #for local machine development
   OPENAI_KEY =os.getenv('OPENAI_API_KEY')
else:
    OPENAI_KEY =st.secrets['OPENAI_API_KEY']

# --- Tools ---

website_search= ScrapeWebsiteTool(website='https://www.cpf.gov.sg/member/retirement-income')

scrapetool = ScrapeWebsiteTool(website_url='https://www.cpf.gov.sg/service/sub-categories?category=P_M_RI')

pdf_search=PDFSearchTool(pdf='data\FAQS.pdf')

# --- Agents ---

#Agent 1
research_agent = Agent(
    role="Research Agent",
    goal="Search through the websites based on {customer_question} to find relevant answers",
    allow_delegation=False,
    verbose=True,
    planning=True,
    backstory=(
        """
        The research agent is adept at searching and 
        extracting data from the website, ensuring accurate and prompt responses.
        Provide the information to the customer agent.
        """
    ),
    tools=[website_search,scrapetool,pdf_search],

)

#Agent 2
customer_agent = Agent(
    role="Customer Service Agent",
    goal="Receive information and curate professional customer service response based on the research agent's findings",
    allow_delegation=True,
    verbose=True,
    backstory=(
        """
        The customer service agent has excellent customer service skills and is able to craft 
        clear and concise replies based on the provided information.
        """
    ),
    tools=[website_search,scrapetool,pdf_search],
)


# --- Tasks ---
research_task = Task(
    description=(
        
        """
        Answer the customer inquiry on {customer_question}"" 
        ""The research agent will search through the given websites and PDF to find the relevant answers.""
        "" Use all the tools at your disposal to scrape and find the answers.
        ""Your final answer MUST be clear and accurate, based on the content of websites."""
    ),
    expected_output=
        """
        Provide clear and accurate answers to the customer inquires on""
        the content of the websites. If there are other links related to the inquiry,
        click on the link and find out more information. Relay all information to the Customer Agent.
        Do not make assumptions.
        """
        ,
    tools=[website_search,scrapetool,pdf_search],
    agent=research_agent,
)

reply_task = Task(
    description=(
        """ 
        - Write a polite and concise answer to the customer.""
        - The reply should clearly state the answers found in the specified section.
        - DO NOT ASSUME ANY information. If you do not know, refer the user back to the relevant
         contact details and email address found on the website.
        """
         
    ),
    expected_output=
      """
        Write a clear and concise reply to the customer to address the 
        answers found from the website and also answers from the Research Agent. Sign off
        your name as CPF AI Retirement Bot
        """,
    tools=[website_search,scrapetool,pdf_search],
    agent=customer_agent,
)

# --- Crew ---
crew = Crew(
    agents=[research_agent, customer_agent],
    tasks=[research_task, reply_task],
    full_output=False,
    verbose=0,
    process=Process.sequential,
)

def process_user_message(user_input):
    delimiter = "```"

    output=crew.kickoff(inputs={"customer_question": user_input})
    return output







