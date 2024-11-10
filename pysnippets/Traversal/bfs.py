from collections import deque
from typing import Optional, Dict, List, Any
from data_classes import Graph, SearchResult, NodeColor
from logger_config import setup_logger

logger = setup_logger('bfs')

def breadth_first_search(
    graph: Graph,
    start: Any,
    target: Optional[Any] = None,
    max_depth: Optional[int] = None
) -> SearchResult:
    """
    Enhanced Breadth-First Search implementation
    
    Features:
    - Optional target node for early termination
    - Maximum depth limit
    - Full path tracking
    - Distance tracking
    - Node coloring
    """
    try:
        if start not in graph.nodes:
            raise ValueError(f"Start node {start} not in graph")
        if target and target not in graph.nodes:
            raise ValueError(f"Target node {target} not in graph")
        
        logger.info(f"Starting BFS from node {start}")
        graph.reset_nodes()
        
        visited = []
        distances = {node: float('inf') for node in graph.nodes}
        parents = {node: None for node in graph.nodes}
        
        queue = deque()
        queue.append((start, 0))  # (node, depth)
        graph.nodes[start].color = NodeColor.GRAY
        distances[start] = 0
        
        while queue:
            current_tuple = queue.popleft()
            current, depth = current_tuple
            visited.append(current)
            
            if max_depth is not None and depth >= max_depth:
                logger.info(f"Reached max depth {max_depth}")
                break
                
            if target and current == target:
                logger.info(f"Target {target} found at depth {depth}")
                break
            
            for neighbor in graph.nodes[current].neighbors:
                neighbor_node = graph.nodes[neighbor]
                if neighbor_node.color == NodeColor.WHITE:
                    neighbor_node.color = NodeColor.GRAY
                    distances[neighbor] = distances[current] + 1
                    parents[neighbor] = current
                    queue.append((neighbor, depth + 1))
            
            graph.nodes[current].color = NodeColor.BLACK
            logger.debug(f"Processed node {current} at depth {depth}")
        
        return SearchResult(visited, distances, parents)
        
    except Exception as e:
        logger.error(f"Error in BFS: {str(e)}")
        raise

def bfs_level_order(graph: Graph, start: Any) -> Dict[int, List[Any]]:
    """Returns nodes grouped by their levels from start node"""
    result = breadth_first_search(graph, start)
    levels: Dict[int, List[Any]] = {}
    
    for node, dist in result.distances.items():
        if dist != float('inf'):
            if dist not in levels:
                levels[dist] = []
            levels[dist].append(node)
            
    return levels

def find_shortest_path(graph: Graph, start: Any, end: Any) -> Optional[List[Any]]:
    """Find shortest path between start and end nodes"""
    result = breadth_first_search(graph, start, target=end)
    
    if result.distances[end] == float('inf'):
        return None
        
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = result.parents[current]
    return path[::-1]