from dotenv import load_dotenv
import os

_DISALLOWED_CHARACTERS = ["/", 
                          "\\", 
                          "\n", 
                          " ", 
                          "   ",
                          "."]


def load_chat_gpt_api_enviroment():
    '''
    Load the chat gpt enviroment variable from the .env file
    '''
    load_dotenv("../api_keys.env")
    return os.getenv("OPENAI_API_KEY")

def add_open_ai_api_key(file_name, open_ai_api_key):
    '''
    Make or append the apps .env to have the specified Open AI API Key
    '''
    safe_file_name = _remove_unwanted_characters(file_name)
    safe_api_key = _remove_unwanted_characters(open_ai_api_key)
    f = open(f"../{safe_file_name}.env", "append")
    f.write(f"OPENAI_API_KEY = {safe_api_key}")
    f.close()

def _remove_unwanted_characters(text):
    safe_text = text.strip()
    for character in _DISALLOWED_CHARACTERS:
        safe_text = safe_text.replace(character, "")

    return safe_text