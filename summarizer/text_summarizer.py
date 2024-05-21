from .long_summarizer import *
from .short_summarizer import *

def create_transcript_summary(transcript):
    thesis, long_bullet_list, conclusion = create_long_text_summary(transcript)

    short_bullet_list = []
    for bullet in long_bullet_list:
        short_bullet_list.append(create_short_text_summary(bullet))

    return thesis, long_bullet_list, short_bullet_list, conclusion