from dataclasses import dataclass
from typing import List, Optional
from nltk.tokenize import word_tokenize, sent_tokenize

@dataclass
class TokenizationResult:
    words: Optional[List[str]] = None
    sentences: Optional[List[str]] = None

def tokenize_text(text: str) -> TokenizationResult:
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    return TokenizationResult(words=words, sentences=sentences) 