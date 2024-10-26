# Capstone Project for AI Bootcamp
## CPF Retirement App

The CPF Retirement App is a capstone project for GovTech's AI Bootcamp 2024
For this project, I have chosen to challenge myself using CrewAI and Streamlit. It is a multi-page app, with 2 use cases.

## Features/Use Case
### CPF Retirement Query
- User will be able to enter the questions/queries into the textbox
- Once the Submit button is clicked, the CrewAI agents get to work, using the PDF and ScrapeWebsiteTool to obtain information. The data in the PDF has been derived from the CPF Retirement FAQs page. Due to the sheer number of questions, I have randomly picked a few common ones to use as dummy data. 
- The agent will reply in _st.markdown_ format.

### Retirement Planner
- Users will be able to input their current age and their desired present day monthly retirement income using sliders. The future value income will be calculated with an assumed inflation rate of 2%. This will also take into account the number of years left before the reach the age of 65.
- Once the Get Goal button is clicked, the future value is calculated.The CrewAI agents get to work, using the PDF, DOCX search tools and ScrapeWebsiteTool to come up with a practical financial plan. For this event, it may take a few minutes for the agents to generate the retirement plan. 

## Other Pages
### About This App
- This page shows the project scope, objectives and data sources. It also talks about the features and how to use the CPF Retirement Query and Retirement Planner.
- ### Methodology
- This page shows the flowchart for both use cases.


## Tech

The app was developed using:

- [VS Code] - IDE
- [CrewAI] - AI Agents
- [Streamlit] - Python UI library for Data/LLM apps
- [Streamlit Community Cloud] - Platform for hosting the app

## Notes

The app may face issues running on Streamlit Cloud. Due to this I have attached a video demo of how it is intended to work. *Apologies for this as I am quite new to coding and development.*

You can view the video on 
https://drive.google.com/file/d/1NIspX0EQnRdSLZc6MxJcM8EQ9GzK47BY/view?usp=drive_link

## Thank you and have a nice day!








