from constants import chat_gpt_constants
from utils import api_utils
from langchain_openai import ChatOpenAI
from properties import chat_gpt_properties

OPENAI_MODEL = chat_gpt_constants.get_chat_gpt_version()
OPENAI_API_KEY = api_utils.load_chat_gpt_api_enviroment()
SUMMARY_TEMP = chat_gpt_properties.DEFAULT_TEMPERATURE
 
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, temperature=SUMMARY_TEMP)



