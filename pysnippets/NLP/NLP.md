Here is a sample README for the advanced NLP code snippets, describing each snippet in detail, along with instructions for setup, usage, and testing.

---

# Advanced NLP Code Snippets

This repository provides a collection of advanced Natural Language Processing (NLP) code snippets in Python. Each snippet covers essential NLP tasks such as tokenization, stemming, lemmatization, named entity recognition, text classification, topic modeling, and more. The code is modular, with error handling and data classes for structured inputs and outputs, allowing for easy use, modification, and testing.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Code Snippets](#code-snippets)
4. [Testing](#testing)
5. [Usage Examples](#usage-examples)
6. [Contributing](#contributing)

## Features

- **Error Handling**: Each function handles exceptions gracefully, allowing for safer use with diverse input data.
- **Data Classes**: Used for structured inputs and outputs, making code cleaner and easier to understand.
- **Modular Design**: Code is modular, with each function focused on a specific NLP task, simplifying integration and testing.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/advanced-nlp-snippets.git
   cd advanced-nlp-snippets
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Make sure to install the following additional NLP resources (if not already installed):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

## Code Snippets

### 1. Preprocessing with Stopwords Removal
Removes common stopwords from the text to reduce noise.

```python
def preprocess_text(text: str) -> Optional[str]:
    ...
```

### 2. Tokenization (Word and Sentence)
Splits text into words and sentences, using NLTK's `word_tokenize` and `sent_tokenize`.

```python
@dataclass
class TokenizationResult:
    words: Optional[List[str]] = None
    sentences: Optional[List[str]] = None

def tokenize_text(text: str) -> TokenizationResult:
    ...
```

### 3. Stemming with Porter Stemmer
Reduces words to their root form using the Porter stemmer algorithm.

```python
def stem_text(text: str) -> Optional[str]:
    ...
```

### 4. Lemmatization with WordNet Lemmatizer
Converts words to their base form using NLTK’s WordNet Lemmatizer.

```python
def lemmatize_text(text: str) -> Optional[str]:
    ...
```

### 5. Named Entity Recognition (NER) with spaCy
Extracts named entities (e.g., people, organizations, locations) from text using spaCy.

```python
def extract_entities(text: str) -> Optional[List[Tuple[str, str]]]:
    ...
```

### 6. TF-IDF Vectorization
Transforms a set of documents into TF-IDF feature vectors.

```python
def tfidf_vectorize(documents: List[str]) -> Optional[Any]:
    ...
```

### 7. Word2Vec Similarity
Calculates semantic similarity between two words using Word2Vec.

```python
def word2vec_similarity(word1: str, word2: str, model_path: str) -> Optional[float]:
    ...
```

### 8. Text Classification with Naive Bayes
Builds a Naive Bayes classifier for text data, using TF-IDF for feature extraction.

```python
@dataclass
class TextClassificationResult:
    classifier: Optional[MultinomialNB] = None
    vectorizer: Optional[CountVectorizer] = None

def train_text_classifier(documents: List[str], labels: List[int]) -> TextClassificationResult:
    ...
```

### 9. Topic Modeling with LDA
Performs topic modeling using Latent Dirichlet Allocation (LDA) on a set of documents.

```python
@dataclass
class LDAResult:
    topics: Optional[Any] = None

def lda_topic_modeling(documents: List[str], n_topics: int = 2) -> LDAResult:
    ...
```

### 10. Text Summarization using Gensim
Summarizes a long document using Gensim's `summarize`.

```python
def summarize_text(text: str) -> Optional[str]:
    ...
```

### 11. Cosine Similarity between Texts
Calculates cosine similarity between two text documents.

```python
def cosine_similarity_texts(text1: str, text2: str) -> Optional[float]:
    ...
```

### 12. Text Generation using Markov Chain
Generates new text based on a Markov chain model from the input text.

```python
@dataclass
class MarkovChainText:
    generated_text: Optional[str] = None

def generate_text(text: str, n: int = 3) -> MarkovChainText:
    ...
```

### 13. POS Tagging with spaCy
Extracts parts of speech tags for each word in a sentence using spaCy.

```python
def pos_tagging(text: str) -> Optional[List[Tuple[str, str]]]:
    ...
```

## Testing

Unit tests are provided for each code snippet using Python's `unittest` framework. The test cases ensure that each function works as expected and handles edge cases.

To run the tests:

```bash
python -m unittest discover
```

Example of a test case for `preprocess_text`:

```python
class TestNLP(unittest.TestCase):
    def test_preprocess_text(self):
        text = "This is a sample text with stopwords"
        result = preprocess_text(text)
        self.assertIsInstance(result, str)
    ...
```

## Usage Examples

Below are usage examples for some of the key functions:

```python
# Example usage of preprocess_text
text = "This is a sample text with various stopwords."
processed_text = preprocess_text(text)
print("Processed Text:", processed_text)

# Example usage of word2vec_similarity
similarity = word2vec_similarity("cat", "dog", model_path="path/to/word2vec.bin")
print("Word2Vec Similarity:", similarity)

# Example usage of lda_topic_modeling
documents = ["This is a document about cats.", "This is a document about dogs."]
lda_result = lda_topic_modeling(documents)
print("LDA Topics:", lda_result.topics)
```
