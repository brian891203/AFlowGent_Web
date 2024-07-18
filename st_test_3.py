import streamlit as st
import requests
import json
import time

def chat_with_ollama():
    """
    A Streamlit app that allows users to chat with an Ollama-like assistant.

    The app sends user messages to a local Ollama service and displays the assistant's responses.

    Usage:
    1. Run the Streamlit app.
    2. Enter a message in the chat input box.
    3. Press Enter or click the Send button to send the message.
    4. The assistant's response will be displayed in the chat area.

    Dependencies:
    - streamlit
    - requests
    - json
    - time
    """

    st.title("ChatGPT-like clone with Ollama")

    # Local Ollama service URL
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

        # Create a text area for incremental content updates
        text_area = st.empty()
        response_content = ""

        with st.chat_message("assistant"):
            # Build request payload
            payload = {
                "model": "mistral",
                "messages": [{"role": "user", "content": prompt}]
            }

            # Send request to local Ollama service
            response = requests.post(ollama_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

            if response.status_code == 200:
                try:
                    # Process each line of the JSON response and display the content incrementally
                    for line in response.text.splitlines():
                        message_obj = json.loads(line)
                        if "message" in message_obj and "content" in message_obj["message"]:
                            response_content += message_obj["message"]["content"] + " "
                            text_area.markdown(response_content.strip())
                            time.sleep(0.1)  # Simulate delay for incremental display

                    # Add the final complete response to the session state
                    st.session_state.messages.append({"role": "assistant", "content": response_content.strip()})
                except json.JSONDecodeError as e:
                    st.error(f"JSON decode error: {e.msg}")
                    st.write("Raw response:", response.text)
            else:
                st.error("Failed to get response from Ollama service: " + response.json().get("error", "Unknown error"))

# Run the chat app
chat_with_ollama()
