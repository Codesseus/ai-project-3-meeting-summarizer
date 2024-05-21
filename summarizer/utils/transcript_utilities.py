# Project_3_Research\Resources\Output_Text\Example_1_no_timestamps.txt

def get_transcript_text(file_name):
    f = open(f"../Project_3_Research/Resources/Output_Text/{file_name}.txt")
    text = f.read()
    f.close()
    return text

def remove_timestamp_from_line(line_of_text):
    """
    Arguments: (string) line_of_text
    return: (string)

    This function takes a line of text and removes the timestamp.
    It returns a new string with the timestamp removed.

    NOTE: This assumes that the timestamp will be contained within the first starting square brackets
    and the last ending square brackets.
    This will remove all the text from the first index of '[' to the last index of ']'.
    If it cannont find either symbol it will return the original line of text.
    """
    #Get the index of the starting square bracket '[', if its -1 then we return since there is no timestamp
    starting_bracket_index = line_of_text.find("[")
    if starting_bracket_index == -1:
        return line_of_text

    #Get the index of the first occurance of the ending square bracket ']', if its -1 then we return since there is no timestamp
    ending_bracket_index = line_of_text.find("]")
    if ending_bracket_index == -1:
        return line_of_text
    
    searching_for_index = True
    #Loop to find the last index of the ending bracket
    while searching_for_index:
        #Continue to work on this, need to make sure that we dont get stuck in an infinite loop
        if ending_bracket_index + 1 < len(line_of_text):
            new_index = line_of_text.find("]", ending_bracket_index + 1)
            if new_index == -1:
                searching_for_index = False
            if new_index > ending_bracket_index:
                ending_bracket_index = new_index

        # searching_for_index = False
        #TODO: Keep Working on this


    




