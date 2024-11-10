from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from typing import List

def train_text_classifier(documents: List[str], labels: List[int]):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents)
    classifier = MultinomialNB()
    classifier.fit(X, labels)
    return classifier, vectorizer 