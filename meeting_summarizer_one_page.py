# Run command
#streamlit run meeting_summarizer_one_page.py --server.enableCORS=false
#streamlit run meeting_summarizer_one_page.py --server.enableXsrfProtection false

import streamlit as st

# Converts video to text with time stamps.
from transcription_functions import transcribe_video_to_text

#Summarization Model - Provides summary, short and long bullet points
from summarizer.text_summarizer import create_transcript_summary
import os

st.set_page_config(
    layout="wide",
    page_title="Meeting Summarizer",
    #page_icon="👋",
)

#Initialize Variables
bullet_points = []
file_name = ""

#Display the Welcome Message
st.write("""# Welcome to Meeting Summarizer 
### Web-Based Application to summarize meetings. 
### Project 3 ASU AI Course: Cody Cushing, Sergio Garzon and David Gerhart         
##### Version .1 
         Select Meeting Video file to upload. The transcribed and summarized for your review."
         """)

def play_from_time(audio_file, start_time):
  # Load audio
  y, sr = librosa.load(audio_file)

  # Extract portion from start_time onwards
  audio_segment = y[int(start_time*sr):]

  # Play audio segment
  sd.play(audio_segment, sr)

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
        audio_file, text_with_timestamps = transcribe_video_to_text(video_file)
        st.session_state["text_with_timestamps"] = text_with_timestamps
        st.session_state["audio_file"] = audio_file

        #Send the text to the summarizer and cache the results and get an array of bullet points back
        thesis, long_bullet_list, short_bullet_list, conclusion = create_transcript_summary(text_with_timestamps)

        # Insert blank line as first bullet point
        short_bullet_list.insert(0, "")
        long_bullet_list.insert(0, "")

        #Save bullet points in session state
        st.session_state["thesis"] = thesis
        st.session_state["bullet_points"] = short_bullet_list
        st.session_state["bullet_points_long"] = long_bullet_list

        st.write("Processing Complete...")

# Display Summary
if 'thesis' in st.session_state:
    summary = st.session_state["thesis"]
    st.write(f"##### Summary: {summary}")


#Use cached bullet points if they exist
if 'bullet_points' in st.session_state:
    bullet_points = st.session_state["bullet_points"]

# Display the bullet points
#selected_bullet = st.selectbox("Select a bullet point to learn more:", bullet_points)
index = st.selectbox("Select Bullet Point", range(len(bullet_points)), format_func=lambda x: bullet_points[x])
        
# Show Options when a bullet point is selected
if index:
    # Display the selected bullet point (no need)
    #st.write(f"You selected: {bullet_points[index]}")
        
    # Show the bullet points in a single row
    col1, col2, col3 = st.columns(3)        

    with col1:
        if st.button("Watch More"):
            video_file = st.session_state["video_file"]
            st.title('Play Portion of Video')

            # Display the video player with the specified start and end times
            st.video(video_file, start_time=25, end_time=45)

    with col2:
        if st.button("Listen to More"):
            audio_file = st.session_state["video_file"]
            st.audio(audio_file, start_time=45)

    with col3:
        if st.button("Read More"):
            #Retrieve long bullet point
            text = st.session_state["bullet_points_long"][index]
            #Find position of the time stamp
            time_stamp_position = text.find("[")
            #Display the text after time stamp removed
            st.write(text[0:time_stamp_position])
        


        


