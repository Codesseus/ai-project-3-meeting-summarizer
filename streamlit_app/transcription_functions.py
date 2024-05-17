import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from moviepy.editor import VideoFileClip
from datetime import datetime

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

""" Having trouble getting files to upload to different folders
def upload_and_redirect_file(file, target_folder):

    if file is not None:
        with open(os.path.join(target_folder, file), "wb") as f:
            f.write(file.getvalue())
    return file
           #st.success(f"File '{file.name}' uploaded successfully to '{target_folder}'.")
"""

# Method to Transcribe audio with time stamps
# Source: https://community.openai.com/t/how-to-get-whispers-api-to-add-timestamps-to-the-transcripts/501788



# Transcribe audio witout time stamps
def transcribe_audio_no_time_stamps(client, audioFile):
    audio_file = open(audioFile, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcript.text


# transcribe audio with time stamps
def transcribe_audio_with_time_stamps(client, audioFile):
    with open(audioFile, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="srt"
        )
        # Pass the transcription directly for processing
        return process_transcription(transcription)
        # return response  # Directly return the response, assuming it's the transcription text


def format_time(time):
    time_obj = datetime.strptime(time, "%H:%M:%S,%f")
    return time_obj.strftime("%H:%M:%S")

# Function to process the raw transcription into the desired format
def process_transcription(transcription):
    blocks = transcription.split('\n\n')
    processed_lines = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            time_range = lines[1]
            text = lines[2]
            start_time = time_range.split(' --> ')[0]
            # Convert the time format from "00:00:00,000" to "0:00:00"
            formatted_start_time = format_time(start_time)
            processed_line = f"[{formatted_start_time}]{text}"
            processed_lines.append(processed_line)
    return '\n'.join(processed_lines)
 
# Transcribe video to text
def transcribe_video_to_text(video_file):
   
    # Load the video file
    video = VideoFileClip(video_file)

    # Extract the audio from the video
    audio = video.audio

    # Create a file name for the audio file
    audioFile = video_file.replace('.mp4', '.mp3')

    # Save the audio file
    #Use this when saving to a different folder audio.write_audiofile(f"{audioFolder}{audioFile}")
    if not(os.path.exists(audioFile)):
        audio.write_audiofile(audioFile)

    #Cloe and release the video file
    video.close()

    # Transcribe audio with time stamps
    #Use this when reading from  a different folders transcript_with_timestamps = transcribe_audio_with_time_stamps(
    #client, f"{audioFolder}{audioFile}")
    transcript_with_timestamps = transcribe_audio_with_time_stamps(client, audioFile)

    return transcript_with_timestamps


