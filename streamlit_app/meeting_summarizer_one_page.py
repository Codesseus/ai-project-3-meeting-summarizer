# Run command
#streamlit run meeting_summarizer_one_page.py --server.enableCORS=false
#streamlit run meeting_summarizer_one_page.py --server.enableXsrfProtection false

import streamlit as st
from transcription_functions import transcribe_video_to_text
import os

st.set_page_config(
    layout="wide",
    page_title="Meeting Summarizer",
    #page_icon="👋",
)

#Initialize Variables
bullet_points = []
file_name = ""

@st.cache_data
def summarize_text(text_with_timestamps):
    bullet_points = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "Life is like riding a bicycle. To keep your balance, you must keep moving.",
        "In the middle of difficulty lies opportunity.",
        "The only way to do great work is to love what you do.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall."
    ]
    return bullet_points

st.write("""# Welcome to Meeting Summarizer 
### Web-Based Application to summarize meetings. 
### Project 3 ASU AI Course: Cody Cushing, Sergio Garzon and David Gerhart         
##### Version .1 
         Select Meeting Video file to upload. The transcribed and summarized for your review."
         """)


container_1 = st.empty()
with container_1:
    uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False, type=["mp4"])
    # Use if able to get uloading and loading in different folders to work
    #uploaded_file = upload_and_redirect_file(file_name, videoFolder)


if uploaded_file is not None:  
    st.write("File uploaded. Click Transcribe Uploaded Video to begin processing.")
    file_name = uploaded_file.name
    #Debug file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    #Debug st.write(f"#### Video File Received :blue[{file_name}]")
    #Debug st.write(file_details)

    # Specify the folder where you want to save the uploaded file
    save_folder = "uploads"

    # Create the folder if it doesn't exist
    if not os.path.exists(save_folder):
        #Debug st.write(f"making path {save_folder}")
        os.makedirs(save_folder)

    # Join the folder path with the filename
    video_file = os.path.join(save_folder, uploaded_file.name)

    # Save the uploaded file to the specified folder
    with open(video_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Save the path to the video file in the session state
    st.session_state["video_file"] = video_file



#Transcribe Text from the video, get bullet points and display them
if st.button("Transcribe Uploaded Video"):

    video_file = ""

    # Get video file path from the session state
    if 'video_file' in st.session_state:
        video_file = st.session_state["video_file"]
    
    if(video_file == ""):
        st.write("No video file uploaded. Please upload a video file first.")
    else:
        st.write("Processing Video...")
        text_with_timestamps = transcribe_video_to_text(video_file)

        #Send the text to the summarizer and cache the results and get an array of bullet points back
        bullet_points = summarize_text(text_with_timestamps)
        st.session_state["bullet_points"] = bullet_points
        st.write("Processing Complete...")

 
#Use cached bullet points if they exist
if 'bullet_points' in st.session_state:
    bullet_points = st.session_state["bullet_points"]

# Display the bullet points
selected_bullet = st.selectbox("Select a bullet point to learn more:", bullet_points)
        
# Show Options when a bullet point is selected
if selected_bullet:
    st.write("You selected:", selected_bullet)
        
    # Show the bullet points in a single row
    col1, col2, col3 = st.columns(3)        

    with col1:
        if st.button("Watch More"):
            video_file = st.session_state["video_file"]
            st.title('Play Portion of Video')


            # Display the video player with the specified start and end times
            st.video(video_file, start_time=25, end_time=45)

    with col2:
        if st.button("Read More"):
            st.write("Will Display more text")
        
    with col3:
        if st.button("Listen to More"):
            st.write("Will play audio")
        


