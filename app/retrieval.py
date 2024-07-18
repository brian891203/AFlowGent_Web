import streamlit as st

def render_next_node_page():
    st.title("Next Node")
    st.write("This is the next node page.")
    if st.button("Go Back"):
        st.session_state.page = "question_classification"
        st.rerun()
