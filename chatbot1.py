import streamlit as st
import openai
import os

# Set your OpenAI API key as an environment variable
# For example, in your terminal: export OPENAI_API_KEY='your_api_key'
openai.api_key = os.getenv('OPENAI_API_KEY')

system_message = {
    "role": "system",
    "content": '''
You are a chatbot for a software company. Greet users, introduce yourself as an AI chatbot, and ask for their question.
Answer in a short, clear manner. Use the following company info as needed:

Company details:
- Name: New Creations
- Address: Aldie, Virginia
- Contact: 9876543210
- Hiring: Yes. Apply via softwaresolutions.com or LinkedIn.
- Industry: IT consulting and staffing
- Business hours: 9 am to 5 pm EST
- Email: softwaresolutions@gmail.com
- Clients: Mission Company, Tech Solutions, OneSolutions
- 6 years in business, ~100 employees.

Remember the chat history to improve your answers each time.
'''
}

# Set up Streamlit UI
st.set_page_config(page_title="Company Chatbot", page_icon="🤖")
st.title("🤖 New Creations Company Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = [system_message]

def get_completion(messages, model="gpt-3.5-turbo"):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

user_input = st.text_input("What is your question?", key="user_input")
if st.button("Send") and user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    bot_reply = get_completion(st.session_state['messages'])
    st.session_state['messages'].append({"role": "assistant", "content": bot_reply})
    st.rerun()

# Display conversation
for msg in st.session_state['messages'][1:]: # Skip the system message
    if msg['role'] == 'user':
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")