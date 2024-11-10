from dataclasses import dataclass, field
from typing import Dict, Set, Optional, Any, List
from enum import Enum

class NodeColor(Enum):
    WHITE = "white"  # Unvisited
    GRAY = "gray"   # Being visited
    BLACK = "black" # Visited

@dataclass
class Node:
    """Represents a node in a graph with additional metadata"""
    id: Any
    neighbors: Set[Any] = field(default_factory=set)
    color: NodeColor = NodeColor.WHITE
    distance: float = float('inf')
    parent: Optional[Any] = None
    discovery_time: int = 0
    finish_time: int = 0
    
    def __post_init__(self):
        if self.neighbors is None:
            self.neighbors = set()

@dataclass
class Graph:
    """Advanced graph data structure supporting both directed and undirected graphs"""
    nodes: Dict[Any, Node] = field(default_factory=dict)
    directed: bool = False
    weighted: bool = False
    weights: Dict[tuple[Any, Any], float] = field(default_factory=dict)
    
    def add_node(self, node_id: Any) -> None:
        """Add a node if it doesn't exist"""
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)
    
    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        """Add an edge between nodes with optional weight"""
        self.add_node(u)
        self.add_node(v)
        
        self.nodes[u].neighbors.add(v)
        if self.weighted:
            self.weights[(u, v)] = weight
            
        if not self.directed:
            self.nodes[v].neighbors.add(u)
            if self.weighted:
                self.weights[(v, u)] = weight
    
    def get_weight(self, u: Any, v: Any) -> float:
        """Get weight of edge (u,v)"""
        return self.weights.get((u, v), float('inf'))
    
    def reset_nodes(self) -> None:
        """Reset all nodes to initial state"""
        for node in self.nodes.values():
            node.color = NodeColor.WHITE
            node.distance = float('inf')
            node.parent = None
            node.discovery_time = 0
            node.finish_time = 0

@dataclass
class SearchResult:
    """Stores result of graph search algorithms"""
    visited: List[Any]
    distances: Dict[Any, float]
    parents: Dict[Any, Optional[Any]]
    discovery_times: Dict[Any, int] = field(default_factory=dict)
    finish_times: Dict[Any, int] = field(default_factory=dict)