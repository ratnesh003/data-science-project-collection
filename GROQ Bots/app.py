import os
from groq import Groq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

models = client.models.list()
available_models = [x.to_dict()["id"] for x in models.data]

system_prompt = "You are a part of chatbot application, where multiple chatbots are available for user to select. You are a helpful assistant currently selected by user. Your major task is to help user with his queries"

if "models" not in st.session_state:
    st.session_state.models = available_models

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
    ]

if "selected_model" not in st.session_state:
    st.session_state.selected_model = ''

st.set_page_config(layout="wide")

selected_model = st.sidebar.selectbox(
    label="Select Model",
    options=st.session_state.models,
)

if selected_model != st.session_state.selected_model:
    st.session_state.selected_model = selected_model

st.header("Hey! 👋 I am GROQ Bot")

if selected_model:
    st.markdown(f"##### You are talking to **```{selected_model}```**")

    if st.sidebar.button("Clear History", icon=':material/delete:', type="primary", help="Bot will forget what ever you talked" ):
        st.session_state.messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
        ]

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])

    if prompt := st.chat_input("Ask anything to me"):

        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            response = client.chat.completions.create(
                messages=st.session_state.messages,
                model=selected_model,
            )
            response = response.choices[0].message.content
        except :
            response = "Model is having some issue it cann't answer now select any other model"

        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)