import openai
import streamlit as st

st.title("ChatGPT-like clone with Azure OpenAI")
# st.write(st.secrets)

# Azure OpenAI API 的基本設置
openai.api_base = "https://api-csd-lab-je.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"
# openai.api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = "2933c0c5028844ac83b5071171cb9a5f"
api_version = "2024-02-15-preview"
deployment_id = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            engine=deployment_id,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            max_tokens=800,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0,
            top_p=0.95,
            api_version=api_version,
        ).choices[0].message["content"]
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
