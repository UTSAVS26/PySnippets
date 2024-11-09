from nltk.stem import PorterStemmer

def stem_text(text: str) -> str:
    stemmer = PorterStemmer()
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words) 