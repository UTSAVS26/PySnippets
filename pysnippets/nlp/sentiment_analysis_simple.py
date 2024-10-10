#sentiment_analysis_simple.py

from textblob import TextBlob

def sentiment_analysis_simple(text):
    """
    Analyze the sentiment of a given text (positive, negative, neutral).

    Args:
        text (str): The text to analyze sentiment for.

    Returns:
        str: The sentiment classification ('Positive', 'Negative', 'Neutral').

    Example:
        >>> sentiment_analysis_simple("I love this product!")
        'Positive'
    """
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "Positive"
    elif blob.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
if __name__ == "__main__":
    text = "This is an amazing experience!"
    sentiment = sentiment_analysis_simple(text)
    print("Sentiment:", sentiment)
