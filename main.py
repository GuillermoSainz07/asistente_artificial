import streamlit as st
import google.generativeai as genai

import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

#PROMT_CONSTANT = " Incluye la referencia de la informacion que proporcionas y el titulo del documento o los documentos de los cuales obtuviste la informacion."
PROMT_CONSTANT = " Incluye la referencia en formato APA"

st.title("💬🤖 Asistente Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Como puedo ayudarte?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    sample_file = genai.upload_file(path="codigo-fiscal-del-estado-de-sinaloa.pdf",
                                display_name="Gemini 1.5 PDF")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = model.generate_content([sample_file, f"{st.session_state.messages}. {PROMT_CONSTANT}"])

    msg = response.text
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)