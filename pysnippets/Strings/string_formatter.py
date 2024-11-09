import logging
from dataclasses import dataclass
from typing import Dict
import re

logging.basicConfig(level=logging.INFO)

@dataclass
class StringFormatter:
    template: str
    substitutions: Dict[str, str]

    def substitute(self) -> str:
        result = self.template
        for key, value in self.substitutions.items():
            result = result.replace(f'{{{{{key}}}}}', value)
        return result

    def format_with_kwargs(self, **kwargs) -> str:
        return self.template.format(**kwargs)

    def to_snake_case(self, text: str) -> str:
        snake = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
        return snake

    def to_camel_case(self, text: str) -> str:
        components = text.split('_')
        camel = components[0] + ''.join(x.title() for x in components[1:])
        return camel

    def to_pascal_case(self, text: str) -> str:
        components = text.split('_')
        pascal = ''.join(x.title() for x in components)
        return pascal

    def strip_placeholders(self) -> str:
        return re.sub(r'\{.*?\}', '', self.template)

if __name__ == "__main__":
    formatter = StringFormatter(
        template="Hello, {name}! Welcome to {place}.",
        substitutions={"name": "Alice", "place": "Wonderland"}
    )
    substituted = formatter.substitute()
    logging.info(f"Substituted: {substituted}")
    
    formatted = formatter.format_with_kwargs(name="Bob", place="Builderland")
    logging.info(f"Formatted with kwargs: {formatted}")
    
    snake = formatter.to_snake_case("convertToSnakeCase")
    logging.info(f"Snake Case: {snake}")
    
    camel = formatter.to_camel_case("convert_to_camel_case")
    logging.info(f"Camel Case: {camel}")
    
    pascal = formatter.to_pascal_case("convert_to_pascal_case")
    logging.info(f"Pascal Case: {pascal}")
    
    stripped = formatter.strip_placeholders()
    logging.info(f"Stripped Template: {stripped}")