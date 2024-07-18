import streamlit as st
import requests
import json

st.title("ChatGPT-like clone with Ollama")

# 本地 Ollama 服务的 URL
ollama_url = "http://localhost:11434/api/chat"

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
        # 构建请求 payload
        payload = {
            "model": "mistral",
            "messages": [{"role": "user", "content": prompt}]
        }

        # 发送请求到本地 Ollama 服务
        response = requests.post(ollama_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

        # 调试：打印请求和响应
        # st.write("Request payload:", payload)
        # st.write("Response status code:", response.status_code)
        # st.write("Response text:", response.text) 

        if response.status_code == 200:
            response_content = ""
            try:
                # 处理每一行的 JSON 对象
                for line in response.text.splitlines():
                    message_obj = json.loads(line)
                    if "message" in message_obj and "content" in message_obj["message"]:
                        response_content += message_obj["message"]["content"] + " "

                # 去除多余的空格
                response_content = response_content.strip()

                print(response_content)

                # 显示合并后的响应内容
                st.markdown(response_content)
                st.session_state.messages.append({"role": "assistant", "content": response_content})
            except json.JSONDecodeError as e:
                st.error(f"JSON decode error: {e.msg}")
                st.write("Raw response:", response.text)
        else:
            st.error("Failed to get response from Ollama service: " + response.json().get("error", "Unknown error"))
