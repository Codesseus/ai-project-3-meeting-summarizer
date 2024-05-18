from .utils.api_utils import *
from .properties.chat_gpt_properties import *

from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

OPENAI_MODEL = get_chat_gpt_version()
OPENAI_API_KEY = load_chat_gpt_api_enviroment()
SUMMARY_TEMP = DEFAULT_TEMPERATURE

DEBUG = False


def split_and_process_text(text, split_str):
    split_list = text.split(split_str)
    processed_list = []
    i = 0
    for section in split_list:
        if not section == "":
            processed_list.append(section)
            if DEBUG:
                print(f"Section {i}: {section}")
            i += 1
    return processed_list

def create_long_text_summary(transcript_text):
    if DEBUG:
        print(transcript_text)
    
    llm_long_summary = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, temperature=SUMMARY_TEMP)

    long_summary_format = """
    User: Professional people who want technical informattion.
    Context: High detail summary of the provided text. At least 80 words long. The text includes timestamps found within square brackets (i.e. []). Include a thesis paragraph that is a general summary of the text.
    Emotion: No emotion, just information.
    Additional Context: Since the transcription is from a video, refer to the summary as a video.
    Additional Output: Add in paragraghs seperated by bullet points that describe in detail each of the main topics of the video. Each paragraph should be highly detailed and contain 5 or more sentences. At the end of each paragraph include the start and stop time found in the timestamps for the information that lead to this paragraph. If you are unable to determine the start and stop time for the timestamp then write [x-y] instead of the timestamp. Do not include any text after the final paragraph.

    Scribed Text: {transcript}

    Answer: 
    """

    # format = """
    # Transcript: {transcript}

    # You will generate increasingly concise, entity-dense summaries of the above Transcript.

    # Repeat the following 2 steps 5 times.

    # Step 1. Identify 1-3 informative Entites from the Transcript which are missing from teh previously generated summary.
    # Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.

    # A Missing Entity is:
    # - Relevant: to the main story.
    # - Specific: descriptive yet concise (5 words or fewer).
    # - Novel: not in the previous summary.
    # - Faithful: present in the Transcript.
    # - Anywhere: located anywhere in the Transcript.

    # Guidelines:
    # - The first summary should be long (4-5 sentences, ~80 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this video discusses") to reach ~80 words.
    # - Make every word count: re-write the previous summary to improve flow and make space for additional entities.
    # - Make space with fusion, compression, and removal of uninformative phrases like 'the video discusses'.
    # - The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Transcript.
    # - Missing entities can appear anywhere in the new summary.
    # - Never drop entites from the previous summary. If space cannot be made, add fewer new entities.

    # Remember, use the exact same number of words for each summary.

    # Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are "Missing_Entities" and "Denser_Summary"
    # """

    long_summary_prompt_template = PromptTemplate(
        input_variables=["transcript"],
        template=long_summary_format
    )

    chain = LLMChain(llm=llm_long_summary, prompt=long_summary_prompt_template)

    transcript = {f"transcript: {transcript_text}"}

    result = chain.invoke(transcript)

    if DEBUG:
        print(result["text"])

    # Modify the text, break out the overall summary, and each bullet point into its own summary
    long_summary = result["text"]

    

    processed_summary_list = split_and_process_text(long_summary, "\n")

    if DEBUG:
        summary_array = long_summary.split("\n")
        print(summary_array)
        print(len(summary_array))
        print(processed_summary_list)
        print(len(processed_summary_list))

    thesis = processed_summary_list[0]
    bullet_list = []
    conclusion = ""

    if len(processed_summary_list) > 1:
        no_thesis_list = processed_summary_list[1:]
        for section in no_thesis_list:
            #all bullets should end with closing square brakets
            if section.find("]") != -1:
                bullet_list.append(section)
            # the conclusion, if its there, will be after the bullets and will not have square brackets
            else:
                conclusion = section

    return thesis, bullet_list, conclusion