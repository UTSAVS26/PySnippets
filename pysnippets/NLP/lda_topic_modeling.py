from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from typing import List

def lda_topic_modeling(documents: List[str], n_topics: int = 2):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents)
    lda = LatentDirichletAllocation(n_components=n_topics)
    lda.fit(X)
    return lda.components_ 