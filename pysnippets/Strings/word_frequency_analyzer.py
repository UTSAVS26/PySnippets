import logging
from dataclasses import dataclass
from typing import Dict, List
import re
from collections import Counter

logging.basicConfig(level=logging.INFO)

@dataclass
class WordFrequencyAnalyzer:
    text: str
    stop_words: List[str] = None

    def analyze_frequency(self) -> Dict[str, int]:
        words = re.findall(r'\b\w+\b', self.text.lower())
        if self.stop_words:
            words = [word for word in words if word not in self.stop_words]
        return dict(Counter(words))

    def top_n_words(self, n: int) -> List[str]:
        frequency = self.analyze_frequency()
        sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        return [word for word, _ in sorted_words[:n]]

    def unique_words(self) -> List[str]:
        frequency = self.analyze_frequency()
        return [word for word, count in frequency.items() if count == 1]

    def average_word_length(self) -> float:
        words = re.findall(r'\b\w+\b', self.text)
        if not words:
            return 0.0
        total_length = sum(len(word) for word in words)
        return total_length / len(words)

    def filter_by_length(self, min_length: int = 1, max_length: int = None) -> List[str]:
        words = re.findall(r'\b\w+\b', self.text.lower())
        if max_length:
            return [word for word in words if min_length <= len(word) <= max_length]
        return [word for word in words if len(word) >= min_length]

if __name__ == "__main__":
    analyzer = WordFrequencyAnalyzer(
        "Hello world! Hello OpenAI. Welcome to the world of Python. Python is great.",
        stop_words=["to", "the", "of", "is"]
    )
    
    freq = analyzer.analyze_frequency()
    logging.info(f"Word Frequency: {freq}")
    
    top_words = analyzer.top_n_words(3)
    logging.info(f"Top 3 Words: {top_words}")
    
    unique = analyzer.unique_words()
    logging.info(f"Unique Words: {unique}")
    
    avg_length = analyzer.average_word_length()
    logging.info(f"Average Word Length: {avg_length}")
    
    filtered = analyzer.filter_by_length(min_length=5)
    logging.info(f"Words with at least 5 characters: {filtered}")