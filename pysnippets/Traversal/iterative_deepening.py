from typing import Optional, Any
from data_classes import Graph, SearchResult, NodeColor
from logger_config import setup_logger

logger = setup_logger('iterative_deepening')

def iterative_deepening_search(
    graph: Graph,
    start: Any,
    target: Optional[Any] = None,
    max_depth: int = 100
) -> SearchResult:
    """
    Iterative Deepening Depth-First Search
    
    Combines benefits of DFS and BFS:
    - Memory-efficient like DFS
    - Complete like BFS
    - Finds optimal path for unweighted graphs
    """
    try:
        if start not in graph.nodes:
            raise ValueError(f"Start node {start} not in graph")
            
        logger.info(f"Starting IDDFS from node {start}")
        
        visited = []
        distances = {node: float('inf') for node in graph.nodes}
        parents = {node: None for node in graph.nodes}
        
        def dfs_limited(node: Any, depth: int) -> bool:
            visited.append(node)
            graph.nodes[node].color = NodeColor.GRAY
            
            if target and node == target:
                logger.info(f"Target {target} found at depth {depth}")
                return True
                
            if depth <= 0:
                return False
                
            for neighbor in graph.nodes[node].neighbors:
                if graph.nodes[neighbor].color == NodeColor.WHITE:
                    distances[neighbor] = distances[node] + 1
                    parents[neighbor] = node
                    if dfs_limited(neighbor, depth - 1):
                        return True
                        
            graph.nodes[node].color = NodeColor.BLACK
            return False
            
        for depth in range(max_depth):
            logger.debug(f"Trying depth limit: {depth}")
            graph.reset_nodes()
            visited.clear()
            distances[start] = 0
            
            if dfs_limited(start, depth):
                return SearchResult(visited, distances, parents)
                
        logger.info(f"Target not found within max depth {max_depth}")
        return SearchResult(visited, distances, parents)
        
    except Exception as e:
        logger.error(f"Error in IDDFS: {str(e)}")
        raise 