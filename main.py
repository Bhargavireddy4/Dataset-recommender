import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag


nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')


def search_keyword_in_csv(csv_file, keyword, column_name):
    try:
        df = pd.read_csv(csv_file, encoding='latin-1')
    except UnicodeDecodeError:
        print(f"Error decoding the file with 'utf-8' encoding. Trying 'latin-1' encoding...")
        df = pd.read_csv(csv_file, encoding='latin-1')
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
        return []

    # Make the search case-insensitive using regular expressions
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)

    # Use boolean indexing to filter rows where the keyword is found in the specified column
    filtered_df = df[df[column_name].str.contains(pattern, na=False)]

    # Get the row numbers where the keyword is found
    locations = filtered_df.index + 1  # Add 1 to match your row numbering from 1

    return locations

def extract_keywords(sentence):
    # Tokenize the input sentence into words
    words = word_tokenize(sentence)

    # Remove common stopwords (e.g., 'the', 'is', 'a', 'in', etc.)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Use Part-of-Speech (POS) tagging to identify nouns and important words (e.g., verbs, adjectives, adverbs)
    tagged_words = pos_tag(filtered_words)

    # Extract only the nouns and important words
    keywords = [word for word, pos in tagged_words if pos.startswith('N') or pos.startswith('VB') or pos.startswith('JJ') or pos.startswith('RB')]

    return keywords

if 1:
    user_input = input("ENTER YOUR PROMPT: ")
    keywords = extract_keywords(user_input)
    
    print("Keywords:", keywords)
    # Example usage:
    csv_file_path = "C:/Users/bharg/OneDrive/Desktop/NASA Hackathon/keywords.csv"
    df = pd.read_csv(csv_file_path, encoding='latin-1')

    for ikl in keywords:
        keyword_to_search = ikl
        column_to_search = "Column2"  # Replace "Column1" with the actual column name
    
        locations = search_keyword_in_csv(csv_file_path, keyword_to_search, column_to_search)
    
        if len(locations) > 0:
            
            
            print(f"The word '{keyword_to_search}' is found in rows: {', '.join(map(str, locations))}")
            for i in locations:
                print(df['Column1'][i-1])
                print(df['Column3'][i-1])
                print()
        else:
            print(f"The word '{keyword_to_search}' was not found in the specified column.")