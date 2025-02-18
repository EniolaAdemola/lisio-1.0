import os
import streamlit as st
from openai import OpenAI

# Load the environment variables
from dotenv import load_dotenv
load_dotenv()

# initialize the OpenAI client
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# function to get the response from the model
def get_lisio_response(user_message: str) -> str:
    lisio_chat = client.chat.completions.create(
        model="ft:gpt-4o-2024-08-06:personal:lisio-1-0:B2ErupFL",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    ) 
    return lisio_chat.choices[0].message.content

# Streamlit app
def main():
    st.title("Lisio Chatbot")
    st.write("Welcome to Lisio Chatbot! Ask me anything about Appliso Technologies.")
    user_message = st.text_input("Message Lisio: ")

#    When the user submits a message, get the response from the model
    if user_message:
        with st.spinner("Lisio is getting teh answer..."):
            lisio_response = get_lisio_response(user_message)
            st.subheader("Lisio's Answer:")
            st.write("Lisio:", lisio_response)

if __name__ == "__main__":
    main()