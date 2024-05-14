import streamlit as st


st.set_page_config(
    page_title="Meeting Summzrizer",
    #page_icon="👋",
)

st.write("""# 👋 Welcome to Meeting Summarizer 👋
### Web-Based Application to summarize meetings. 
### Project 3 ASU AI Course: Cody Cushing, Sergio Garzon and David Gerhart         
##### Version .1 """)


if st.button(":blue[Click Here] to select a meeting video file with your data to begin"):
    st.switch_page("pages/1 Select data file and init proc.py")


