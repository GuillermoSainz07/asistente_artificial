import streamlit as st
import google.generativeai as genai

import os

PROMT_CONSTANT = " Incluye la referencia en formato APA"

with st.sidebar:
    st.image('logo.png',caption="Proyecto de servicio social FACES. Asistente basado el modelo de lenguaje Gemini, con contexto agregado sobre leyes y codigos utililes para el area \
             de auditoria UAS.",width=200)
    "[Codigo fuente](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"


st.title("💬🤖 AudiBot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Como puedo ayudarte?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
 
    gemini_api_key = os.environ["GEMINI_API_KEY"]

    genai.configure(api_key=gemini_api_key)

    sample_file = genai.upload_file(path="codigo-fiscal-del-estado-de-sinaloa.pdf",
                                display_name="Gemini 1.5 PDF")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = model.generate_content([sample_file, f"{st.session_state.messages}. {PROMT_CONSTANT}"])

    msg = response.text
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)