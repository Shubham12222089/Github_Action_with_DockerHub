import streamlit as st
def get_message():
	return "Automated using CI/CD pipelines."
st.title("Hello, Streamlit!")
st.write(get_message())
