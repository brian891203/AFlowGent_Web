import streamlit as st

with st.sidebar:
    st.title("Navigation")
    # page = st.radio("Go to", ["Main Page", "Question classification", "Retrievel"])
    
# Application title
st.title("Question Classifier")

# Model selection dropdown
model = st.selectbox("Select Model", ["gpt-3.5-turbo CHAT", "gpt-4.0", "gpt-3.0"])

# Initialize category count and input boxes
if 'category_count' not in st.session_state:
    st.session_state['category_count'] = 2

# Render input boxes based on current category count
for i in range(1, st.session_state['category_count'] + 1):
    st.markdown(f"#### Category {i}")
    st.text_input(f"LLM classification description {i}", key=f"category_{i}")

# Add category button
if st.button("Add Category", key='add_button_below'):
    st.session_state['category_count'] += 1
    st.rerun()

# Explanation text
st.markdown("Define the classification conditions of user questions, LLM can define how the conversation progresses based on the classification description.")

# Deploy settings button
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
