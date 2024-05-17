from utils import transcript_utilities

import long_summarizer
import short_summarizer

def create_transcript_summary(transcript):
    thesis, long_bullet_list, conclusion = long_summarizer.create_long_text_summary(transcript)

    short_bullet_list = []
    for bullet in long_bullet_list:
        short_bullet_list.append(short_summarizer.create_short_text_summary(bullet))

    return thesis, long_bullet_list, short_bullet_list, conclusion