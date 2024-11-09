from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Graph:
    vertices: List[str]
    edges: Dict[str, Dict[str, int]] 