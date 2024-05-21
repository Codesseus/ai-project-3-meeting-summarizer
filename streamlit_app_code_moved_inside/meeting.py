class Meeting:
    def __init__(self, title, description, organizer, meeting_duration, meeting_timestamp, invited_list, video_file_name, audio_file_name, text_transcription_without_timestamps, text_transcription_with_timestamps):
        self.title = title
        self.description = description
        self.organizer = organizer
        self.meeting_duration = meeting_duration
        self.meeting_timestamp = meeting_timestamp
        self.invited_list = invited_list
        self.video_file_name = video_file_name
        self.audio_file_name = audio_file_name
        self.text_transcription_without_timestamps = text_transcription_without_timestamps
        self.text_transcription_with_timestamps = text_transcription_with_timestamps
