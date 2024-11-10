from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Optional
import numpy as np
def tfidf_vectorize(documents: List[str]) -> Optional[np.ndarray]:
    vectorizer = TfidfVectorizer()
    return vectorizer.fit_transform(documents).toarray() 