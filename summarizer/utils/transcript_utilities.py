# Project_3_Research\Resources\Output_Text\Example_1_no_timestamps.txt

def get_transcript_text(file_name):
    f = open(f"../Project_3_Research/Resources/Output_Text/{file_name}.txt")
    text = f.read()
    f.close()
    return text