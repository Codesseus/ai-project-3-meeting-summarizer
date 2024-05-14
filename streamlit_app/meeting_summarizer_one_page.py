import streamlit as st
from dotenv import load_dotenv
from utility_functions import upload_and_redirect_file, transcribe_video_to_text
import os

# Video transcription with Whisper
from openai import OpenAI
from moviepy.editor import VideoFileClip

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(
    page_title="Meeting Summzrizer",
    #page_icon="👋",
)

st.write("""# 👋 Welcome to Meeting Summarizer 👋
### Web-Based Application to summarize meetings. 
### Project 3 ASU AI Course: Cody Cushing, Sergio Garzon and David Gerhart         
##### Version .1 
         Select Meeting Video file. The file will be uploaded, transcribed and summarized."
         """)

videoFolder = "resources/source_video/"
audioFolder = "resources/output_audio/"
textFolder = "resources/output_text/"

# initialize variables
if 'file_name' in st.session_state:
    file_name = st.session_state['file_name']

container_1 = st.empty()
with container_1:
    uploaded_file = upload_and_redirect_file(file_name, videoFolder)

if uploaded_file is not None:  
    file_name = uploaded_file.name
    st.session_state['file_name'] = file_name
    st.write(f"#### Working with file :blue[{file_name}]")

textfile_with_timestamps, text_file_without_timestamps = transcribe_video_to_text(uploaded_file, audioFolder, textFolder)

#Calling the model

#display bullet points






