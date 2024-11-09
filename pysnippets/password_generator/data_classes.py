from dataclasses import dataclass

@dataclass
class PasswordConfig:
    length: int = 12
    use_upper: bool = True
    use_lower: bool = True
    use_digits: bool = True
    use_symbols: bool = True
    min_length: int = 8
    max_length: int = 64
    require_upper: bool = True
    require_lower: bool = True
    require_digits: bool = True
    require_symbols: bool = True 