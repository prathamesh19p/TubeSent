from apiclient.discovery import build
from textblob import TextBlob
import re
import statistics
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def get_youtube_service():
    """
    Function to get the YouTube service. It returns the YouTube API service with the specified name and version, using the developer key provided as a parameter.
    """
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    developer_key = "#PutYourKeyHere"
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=developer_key)

def fetch_comments(youtube, video_id):
    """
    Fetches comments from a YouTube video using the YouTube Data API.

    Args:
        youtube: The YouTube Data API object.
        video_id: The ID of the YouTube video.

    Returns:
        A list of comments extracted from the specified YouTube video.
    """
    comments = []
    next_page_token = None
    while True:
        results = youtube.commentThreads().list(
            part="snippet",
            maxResults=100,
            videoId=video_id,
            textFormat="plainText",
            pageToken=next_page_token
        ).execute()
        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
        next_page_token = results.get("nextPageToken")
        if not next_page_token:
            break
    return comments

def clean_comments(comments):
    """
    Clean comments by removing emojis from each comment in the input list.
    
    Parameters:
    comments (list): A list of strings representing comments with emojis.

    Returns:
    list: A list of strings representing the cleaned comments without emojis.
    """
    cleaned_comments = []
    for comment in comments:
        cleaned_comment = remove_emoji(comment)
        cleaned_comments.append(cleaned_comment)
    return cleaned_comments

import re

def remove_emoji(string: str) -> str:
    """
    Remove emoji from the input string.

    Args:
    string (str): The input string containing emoji.

    Returns:
    str: The input string with emoji removed.
    """
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"  
                           u"\U0001F680-\U0001F6FF"  
                           u"\U0001F1E0-\U0001F1FF"  
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def analyze_sentiment(comments):
    """
    Analyze the sentiment of a list of comments using VADER and TextBlob sentiment analysis.
    
    Parameters:
    comments (list of str): The list of comments to analyze.
    
    Returns:
    tuple: A tuple containing the VADER score and TextBlob score for the sentiment analysis.
    """
    sid = SentimentIntensityAnalyzer()
    vader_scores = []
    textblob_scores = []
    for comment in comments:
        vader_score = sid.polarity_scores(comment)['compound']
        textblob_score = TextBlob(comment).sentiment.polarity
        vader_scores.append(vader_score)
        textblob_scores.append(textblob_score)
    vader_score = statistics.mean(vader_scores)
    textblob_score = statistics.mean(textblob_scores)
    return vader_score, textblob_score

def display_sentiment_analysis(vader_score, textblob_score):
    """
    Display the sentiment analysis results using Vader and TextBlob sentiment scores.

    Parameters:
    - vader_score: The sentiment score obtained from the Vader Sentiment Analyzer.
    - textblob_score: The sentiment score obtained from the TextBlob Sentiment Analyzer.

    Return:
    None
    """
    print("Using Vader Sentiment Analyzer:")
    print("Overall Reviews are", get_sentiment_label(vader_score), "with Score {:.2f}%".format(100 * vader_score))
    print()
    print("Using TextBlob Sentiment Analyzer:")
    print("Overall Reviews are", get_sentiment_label(textblob_score), "with Score {:.2f}%".format(100 * textblob_score))

def get_sentiment_label(score):
    """
    Function to determine the sentiment label based on the input score.
    
    Parameters:
    score (int or float): The score used to determine the sentiment label.
    
    Returns:
    str: The sentiment label ("Positive", "Negative", or "Neutral").
    """
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    """
    This function initializes a connection to the YouTube service, prompts the user to enter a video id, 
    fetches comments for the specified video, cleans the comments, analyzes the sentiment of the cleaned comments,
    and displays the sentiment analysis results.
    """
    youtube = get_youtube_service()
    video_id = input("Enter video id: ")
    comments = fetch_comments(youtube, video_id)
    cleaned_comments = clean_comments(comments)
    vader_score, textblob_score = analyze_sentiment(cleaned_comments)
    display_sentiment_analysis(vader_score, textblob_score)

if __name__ == "__main__":
    main()
