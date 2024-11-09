import re
from typing import Dict

def substitute_template(template: str, substitutions: Dict[str, str]) -> str:
    pattern = re.compile(r'{(\w+)}')
    return pattern.sub(lambda match: substitutions.get(match.group(1), match.group(0)), template)

if __name__ == "__main__":
    template = "Hello, {name}! Welcome to {place}."
    substitutions = {"name": "Alice", "place": "Wonderland"}
    result = substitute_template(template, substitutions)
    print(result)
    # Output: Hello, Alice! Welcome to Wonderland. 