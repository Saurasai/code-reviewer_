import streamlit as st

def display_result(text: str):
    st.markdown("### AI Review & Explanation:")
    st.write(text)
