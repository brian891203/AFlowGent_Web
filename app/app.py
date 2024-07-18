import streamlit as st
from question_classification_page import render_classification_page
from retrieval import render_next_node_page

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Main Page", "Question classification", "Retrievel"])

# Main code to render pages based on sidebar selection
if page == "Main Page":
    # render_main_page()
    pass
elif page == "Question classification":
    render_classification_page()
elif page == "Retrievel":
    render_next_node_page()

# # Main code to render pages based on session state
# if 'page' not in st.session_state:
#     st.session_state.page = "question_classification"

# if st.session_state.page == "main":
#     # main_page()
#     pass
# elif st.session_state.page == "question_classification":
#     render_classification_page()
# elif st.session_state.page == "retrieval":
#     render_next_node_page()
