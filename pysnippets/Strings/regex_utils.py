import re
import logging
from dataclasses import dataclass
from typing import List

logging.basicConfig(level=logging.INFO)

@dataclass
class RegexUtils:
    pattern: str
    flags: int = 0

    def find_matches(self, text: str) -> List[str]:
        compiled_pattern = re.compile(self.pattern, self.flags)
        return compiled_pattern.findall(text)

    def replace_matches(self, text: str, replacement: str, count: int = 0) -> str:
        compiled_pattern = re.compile(self.pattern, self.flags)
        return compiled_pattern.sub(replacement, text, count=count)

    def split_text(self, text: str, maxsplit: int = 0) -> List[str]:
        compiled_pattern = re.compile(self.pattern, self.flags)
        return compiled_pattern.split(text, maxsplit=maxsplit)

    def is_match(self, text: str) -> bool:
        compiled_pattern = re.compile(self.pattern, self.flags)
        return bool(compiled_pattern.fullmatch(text))

    def compile_pattern(self) -> re.Pattern:
        return re.compile(self.pattern, self.flags)

if __name__ == "__main__":
    utils = RegexUtils(r'\b\w{4}\b', re.IGNORECASE)
    sample_text = "This is a Test of the regex utilities module."
    
    matches = utils.find_matches(sample_text)
    logging.info(f"Matches: {matches}")
    
    replaced = utils.replace_matches(sample_text, '****')
    logging.info(f"Replaced Text: {replaced}")
    
    split = utils.split_text(sample_text)
    logging.info(f"Split Text: {split}")
    
    match_result = utils.is_match("Test")
    logging.info(f"Is Match: {match_result}")
    
    compiled = utils.compile_pattern()
    logging.info(f"Compiled Pattern: {compiled.pattern}")