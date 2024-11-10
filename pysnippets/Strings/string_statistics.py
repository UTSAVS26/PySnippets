import logging
from dataclasses import dataclass
from typing import Dict
import re

logging.basicConfig(level=logging.INFO)

@dataclass
class StringStatistics:
    text: str

    def __post_init__(self):
        if not isinstance(self.text, str):
            raise ValueError("Text must be a string.")

    def word_count(self) -> Dict[str, int]:
        words = re.findall(r'\b\w+\b', self.text.lower())
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        return count

    def character_frequency(self) -> Dict[str, int]:
        frequency = {}
        for char in self.text:
            frequency[char] = frequency.get(char, 0) + 1
        return frequency

    def sentence_count(self) -> int:
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])

    def average_word_length(self) -> float:
        words = re.findall(r'\b\w+\b', self.text)
        if not words:
            return 0.0
        total_length = sum(len(word) for word in words)
        return total_length / len(words)

    def most_common_word(self) -> str:
        count = self.word_count()
        if not count:
            return ""
        return max(count, key=count.get)

if __name__ == "__main__":
    stats = StringStatistics("Hello world! Hello OpenAI. Welcome to the world of Python.")
    
    word_counts = stats.word_count()
    logging.info(f"Word Counts: {word_counts}")
    
    char_freq = stats.character_frequency()
    logging.info(f"Character Frequency: {char_freq}")
    
    sentence_num = stats.sentence_count()
    logging.info(f"Sentence Count: {sentence_num}")
    
    avg_length = stats.average_word_length()
    logging.info(f"Average Word Length: {avg_length}")
    
    common_word = stats.most_common_word()
    logging.info(f"Most Common Word: {common_word}")