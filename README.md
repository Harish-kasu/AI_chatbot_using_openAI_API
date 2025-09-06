# AI_chatbot_using_openAI_API
Created a chatbot using openai API for a tech software company

Overview
This is a Streamlit-based chatbot application designed for New Creations, an IT consulting and staffing company based in Aldie, Virginia. The chatbot serves as a virtual assistant to answer customer inquiries about the company's services, contact information, hiring opportunities, and general business details.
What This Application Does
The application creates an interactive chat interface where visitors can ask questions about New Creations and receive instant, AI-powered responses. The chatbot maintains conversation history throughout the session, allowing for contextual and relevant answers as the conversation progresses.
Key Features

Interactive Chat Interface: Clean, user-friendly interface built with Streamlit that allows real-time conversation
AI-Powered Responses: Utilizes OpenAI's GPT-3.5-turbo model to generate natural, conversational responses
Context Awareness: Remembers the entire conversation history during a session to provide better, more relevant answers
Company Information Integration: Pre-loaded with essential company details including contact info, business hours, client list, and hiring information
Error Handling: Gracefully handles API errors and displays appropriate error messages

Technical Implementation
The chatbot uses:

Streamlit for the web interface and session management
OpenAI API for natural language processing and response generation
Session State Management to maintain conversation history
Environment Variables for secure API key storage

Company Information Available
The chatbot can answer questions about:

Company location and contact details
Business hours (9 AM - 5 PM EST)
Current hiring status and application process
Industry focus (IT consulting and staffing)
Client portfolio
Company size and history (6 years in business, ~100 employees)

Setup Requirements
To run this application, you'll need:

Python with Streamlit and OpenAI libraries installed
An OpenAI API key (set as an environment variable)
Basic command line knowledge to launch the Streamlit app

This chatbot provides an efficient way for potential clients, job seekers, and general inquiries to get quick answers about New Creations without needing to wait for human support during or outside business hours.RetryClaude can make mistakes. Please double-check responses.
