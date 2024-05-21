from .utils.api_utils import *
from .properties.chat_gpt_properties import *

from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

OPENAI_MODEL = get_chat_gpt_version()
OPENAI_API_KEY = load_chat_gpt_api_enviroment()
SUMMARY_TEMP = DEFAULT_TEMPERATURE

def create_short_text_summary(summary_text):
    llm_short_summary = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, temperature=SUMMARY_TEMP)

    short_summary_format = """
    User: Professional people who want technical informattion.
    Context: A short summary of the provided text. The summary should be 2 sentences or less.
    Emotion: No emotion, just information.
    Additional Context: Since the transcription is from a video, refer to the summary as a video.

    Scribed Text: {text}

    Answer: 
    """

    short_summary_prompt_template = PromptTemplate(
        input_variables=["text"],
        template=short_summary_format
    )

    short_prompt_chain = LLMChain(llm=llm_short_summary, prompt=short_summary_prompt_template)

    short_prompt_chain = LLMChain(llm=llm_short_summary, prompt=short_summary_prompt_template)
    text = {f"text: {summary_text}"}
    result = short_prompt_chain.invoke(text)

    return result["text"]
