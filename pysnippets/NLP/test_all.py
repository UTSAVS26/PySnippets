import unittest
import nltk
from preprocess_text import preprocess_text
from tokenize_text import tokenize_text
from stem_text import stem_text
from lemmatize_text import lemmatize_text
from extract_entities import extract_entities
from tfidf_vectorize import tfidf_vectorize
from lda_topic_modeling import lda_topic_modeling
from word2vec_similarity import word2vec_similarity
from train_text_classifier import train_text_classifier
from cosine_similarity_texts import cosine_similarity_texts
from generate_text import generate_text

# Ensure all NLTK resources are downloaded
nltk.download('punkt')  # Correct resource name for sentence tokenization
nltk.download('wordnet')
nltk.download('stopwords')

class TestNLPFunctions(unittest.TestCase):

    def test_preprocess_text(self):
        text = "This is a sample text with stopwords"
        result = preprocess_text(text)
        expected_result = "sample text stopwords"
        self.assertEqual(result, expected_result)

    def test_stem_text(self):
        text = "running runners runs easily"
        result = stem_text(text)
        expected_result = "run runner run easili"
        self.assertEqual(result, expected_result)

    def test_lemmatize_text(self):
        text = "running better worse cats"
        result = lemmatize_text(text)
        expected_result = "running better worse cat"
        self.assertEqual(result, expected_result)

    def test_extract_entities(self):
        text = "Barack Obama was born in Hawaii."
        result = extract_entities(text)
        expected_result = [('Barack Obama', 'PERSON'), ('Hawaii', 'GPE')]
        self.assertEqual(result, expected_result)

    def test_tfidf_vectorize(self):
        documents = ["the cat sat", "the dog barked"]
        result = tfidf_vectorize(documents)
        self.assertTrue(result.shape[0] == 2)  # Check only the number of documents

    def test_lda_topic_modeling(self):
        documents = ["I love machine learning", "Python is amazing for data science"]
        result = lda_topic_modeling(documents)
        self.assertTrue(result.shape[0] == 2)  # Check only the number of topics

    def test_train_text_classifier(self):
        documents = ["I love Python", "I hate bugs"]
        labels = [1, 0]
        classifier, vectorizer = train_text_classifier(documents, labels)
        result = classifier.predict(vectorizer.transform(["I love coding"]))
        self.assertEqual(result[0], 1)

    def test_cosine_similarity_texts(self):
        text1 = "I love data science"
        text2 = "Data science is amazing"
        result = cosine_similarity_texts(text1, text2)
        self.assertTrue(result > 0.5)

    def test_generate_text(self):
        text = "Data science is awesome. I love coding."
        result = generate_text(text)
        self.assertIn(result, text)

if __name__ == '__main__':
    unittest.main()
