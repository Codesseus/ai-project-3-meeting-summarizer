import re
import nltk
from sentence_transformers import SentenceTransformer
import numpy as np

def find_closest_match(transcript_file, summary_file):
    # Download the required NLTK resources
    nltk.download('punkt')
    
    # Initialize the SentenceTransformer model
    model = SentenceTransformer('bert-base-nli-mean-tokens')

    # Read the transcript file into a string
    with open(transcript_file, 'r') as file:
        file1_contents = file.read()

    # Preprocess the text to remove timestamps and punctuation
    preprocessed_file1 = re.sub(r'\[\d+:\d+:\d+\]', '', file1_contents)
    preprocessed_file1 = re.sub(r'[^\w\s]', '', preprocessed_file1)

    # Split the text into lines
    file1_lines = preprocessed_file1.split('\n')

    # Tokenize each line
    tokenized_lines = [nltk.word_tokenize(line) for line in file1_lines]

    # Read the summary file into a list of lines
    with open(summary_file, 'r') as file:
        file2_contents = file.readlines()

    # Define the bullet character and punctuation pattern
    bullet_char = '- '
    punctuation_pattern = r'[-,\.]+'

    # Tokenize the bullet points
    tokenized_bullet_points = []
    for line in file2_contents:
        if line.startswith(bullet_char):
            cleaned_line = re.sub(punctuation_pattern, '', line.strip())
            tokens = nltk.word_tokenize(cleaned_line)
            tokenized_bullet_points.append(tokens)

    # Convert tokenized text to strings
    bullet_point_str = ' '.join(tokenized_bullet_points[0])
    line_strs = [' '.join(line) for line in tokenized_lines]

    # Compute embeddings
    bullet_point_embedding = model.encode([bullet_point_str])[0]
    line_embeddings = model.encode(line_strs)

    # Find the closest match using cosine similarity
    closest_match_idx = None
    highest_similarity = -1

    for i, line_embedding in enumerate(line_embeddings):
        similarity = np.dot(bullet_point_embedding, line_embedding) / (np.linalg.norm(bullet_point_embedding) * np.linalg.norm(line_embedding))
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_match_idx = i

    # Return the closest match
    if closest_match_idx is not None:
        return {
            "closest_match_idx": closest_match_idx,
            "closest_match_line": tokenized_lines[closest_match_idx]
        }
    else:
        return {
            "closest_match_idx": None,
            "closest_match_line": None
        }

# Example usage:
# result = find_closest_match('Example_1_with_timestamps.txt', 'Example_1_summary.txt')
# print(f"The closest match is at index {result['closest_match_idx']}: {result['closest_match_line']}")
