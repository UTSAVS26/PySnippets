from typing import Optional, Set
from .data_classes import Graph, SearchResult, NodeColor
from .logger_config import setup_logger

logger = setup_logger('dfs')

def depth_first_search(
    graph: Graph,
    start: int,
    target: Optional[int] = None
) -> SearchResult:
    try:
        if start not in graph.nodes:
            raise ValueError(f"Start node {start} not in graph")
            
        logger.info(f"Starting DFS from node {start}")
        
        visited = []
        distances = {node: float('inf') for node in graph.nodes}
        parents = {node: None for node in graph.nodes}
        distances[start] = 0
        
        def dfs_visit(node: int, depth: int) -> bool:
            visited.append(node)
            
            if target and node == target:
                logger.info(f"Target {target} found!")
                return True
                
            for neighbor in graph.nodes[node].neighbors:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = depth + 1
                    parents[neighbor] = node
                    if dfs_visit(neighbor, depth + 1):
                        return True
                        
            logger.debug(f"Finished visiting node {node}")
            return False
            
        dfs_visit(start, 0)
        return SearchResult(visited, distances, parents)
        
    except Exception as e:
        logger.error(f"Error in DFS: {str(e)}")
        raise 