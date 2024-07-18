import streamlit as st
import requests

# 應用程式的標題
st.title("Question Classifier")

# 模型選擇下拉選單
model = st.selectbox("選擇模型", ["gpt-3.5-turbo CHAT", "gpt-4.0", "gpt-3.0"])

# 初始化分類類別和輸入框
if 'category_count' not in st.session_state:
    st.session_state['category_count'] = 2

# 根據當前的分類數量渲染所有輸入框
for i in range(1, st.session_state['category_count'] + 1):
    st.markdown(f"#### 分類 {i}")
    st.text_input(f"LLM classification description {i}", key=f"category_{i}")

# 新增分類按鈕
if st.button("Add Category", key='add_button_below'):
    st.session_state['category_count'] += 1
    st.rerun()

# Explanation text
st.markdown("Define the classification conditions of user questions, LLM can define how the conversation progresses based on the classification description.")

def call_api(category, description):
    url = "http://your-backend-api-url.com/api"  # 替換為你的後端 API URL
    payload = {"category": category, "description": description}
    response = requests.post(url, json=payload)
    return response.json()

# 送出按鈕
if st.button("Deploy settings"):
    data = {}
    for i in range(1, st.session_state['category_count'] + 1):
        data[f"category_{i}"] = st.session_state.get(f"category_{i}", "")
    
    st.write(data) # for test
    # response = call_api(data)
    # st.write(response)

    if all(value for value in data.values()):
        st.success("Settings deployed successfully!")
    else:
        st.error("Please fill in all the fields.")