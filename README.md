# ai-project-3-meeting-summarizer

The meeting summarizer is a web-based streamlit application that can quickly and conviently summarize any video file into a digestible summary. 

When a user uploads a video file the application creates a thesis paragraph about that video (i.e. it summarizes what the video was about as a whole). It also creates several bullet points that give more indepth detail about the main topics of the video. The application sometimes includes a conclusion that summarizes the content of the video. A user can select one of the bullet points to get a longer summary of that bullet point, get the audio from the video associated with that bullet point, or jump to the location in the video that that bullet points corresponds to.

Using this application a user can quickly stay informed on meetings, or can learn the major points of any informational video.

## Technology Used:
- Streamlit (https://streamlit.io/)
- Chatgpt 4.0 turbo (https://chatgpt.com/)
- Whisper (https://openai.com/index/whisper/)
- Sentence Transformer: bert-base-nli-mean-tokens (https://www.sbert.net/)
- Google Collab

## Install and Run
Option A:
1. Go to https://ai-project-3-meeting-summarizer-rttvfhl39dwghbbhc4ywan.streamlit.app/ and run the hosted version.
2. If you want to run the code on its own or the hosted version is down then follow the steps in option B or C.

Option B:
1. Clone repo from github (https://github.com/Codesseus/ai-project-3-meeting-summarizer)
2. Update python to at least version 3.12.3
3. run the following pip installs on terminal in your conda enviroment:
    - pip install streamlit
    - pip install numpy
    - pip install nltk
    - pip install sentence-transformers
    - pip install langchain
    - pip install openai langchain-openai
    - pip install moviepy
4. Set up enviroment keys either through windows enviroment variables, or create a "api_keys.env" file with a variable named "OPENAI_API_KEY" located at "./AI-PROJECT-3-MEETING-SUMMARIZER/summarizer"
5. In your terminal window, in the "AI-PROJECT-3-MEETING-SUMMARIZER" folder type:
    - ```streamlit run meeting_summarizer_one_page.py --server.enableXsrfProtection false```

Option C:
1. Clone repo from github (https://github.com/Codesseus/ai-project-3-meeting-summarizer)
2. Upload the repo to Google Collab
3. In the timestamp_extractor.py file add the following line of code to the top of the file:
    - ```! pip install sentence-transformers```
4. In api_utils file add the following line of code to the top of the file
    - ```! pip install python-dotenv```
5. In transcription_functions.py file add the following lines of code to the top of the file
    - ```! pip install python-dotenv``` 
    - ```! pip install moviepy```
4. create a "api_keys.env" file with a variable named "OPENAI_API_KEY" located at "./AI-PROJECT-3-MEETING-SUMMARIZER/summarizer"
5. Run the following line of code in the terminal:
    - ```streamlit run meeting_summarizer_one_page.py --server.enableXsrfProtection false```

## File Tree
```
.
│   find_closest_match.py
│   find_closest_match_b.py
│   gitignore
│   meeting_summarizer_one_page.py
│   Project_3_SummaryHarvest.ipynb
│   Project_3_TokenizedPrime.ipynb
│   Project_3_TokenizerBySentence.ipynb
│   Project_3_TokenizerBySentence_v2.ipynb
│   Project_3_Tokenize_Summary.ipynb
│   Project_3_Tokenize_SumTrans.ipynb
│   Project_3_Tokenize_Transcription.ipynb
│   README.md
│   requirements.txt
│   timestamp_extractor.py
│   transcription_functions.py
│   tree.txt
│   __init__.py
│
├───.vscode
│       launch.json
│       settings.json
│
├───Project_3_Research
│   │   Project 3 ideas.docx
│   │   Project_3_streamlit_spike.py
│   │   Project_3_Whisper_Research.ipynb
│   │
│   ├───Resources
│   │   ├───Output_Audio
│   │   │       Example_2.mp3
│   │   │       Example_3.mp3
│   │   │
│   │   ├───Output_Text
│   │   │       Example_1_no_timestamps.txt
│   │   │       Example_1_with_timestamps.txt
│   │   │       Example_2_no_timestamps.txt
│   │   │       Example_2_with_timestamps.txt
│   │   │       Example_3_no_timestamps.txt
│   │   │       Example_3_with_timestamps.txt
│   │   │
│   │   └───Source_Video
│   │           Example_1.mp4
│   │           Example_2.mp4
│   │           Example_3.mp4
│   │
│   └───streamlit
├───resources
│   ├───Output_Summary_Audio
│   │       summary2_audio.mp3
│   │       summary_audio.mp3
│   │
│   ├───Output_Sum_BP
│   │       Example_1_summary.txt
│   │       Summary1_test.txt
│   │       summary2.pdf
│   │       summary2.txt
│   │       summary2b.pdf
│   │       summary2c.pdf
│   │       summary2d.pdf
│   │       summary3.pdf
│   │
│   └───Output_Text
│           Example_1_nTS_Token.json
│
├───summarizer
│   │   long_summarizer.py
│   │   short_summarizer.py
│   │   text_summarizer.py
│   │   __init__.py
│   │
│   ├───properties
│   │   │   chat_gpt_properties.py
│   │   │   __init__.py
│   │
│   ├───utils
│   │   │   api_utils.py
│   │   │   transcript_utilities.py
│   │   │   __init__.py
│
├───uploads
│       Example_1.mp3
│       Example_1.mp4
```

## Works Cited:
[1]: How to import a module from a different directory. https://www.geeksforgeeks.org/python-import-module-from-different-directory/

[2]: Perplexity AI, used to lookup information to construct the timestamp extractor. https://www.perplexity.ai/

[3]: ChatGPT, used to lookup general information for how to code sections of the codebase. https://chatgpt.com/