from typing import Tuple, List, Dict
from heapq import heappop, heappush
import math
from data_classes import Graph
from logger_config import logger

def heuristic(node: Tuple[int, int], goal: Tuple[int, int]) -> float:
    """Euclidean distance heuristic."""
    return math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

def a_star(graph: Graph, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[List[Tuple[int, int]], float]:
    try:
        open_set = []
        heappush(open_set, (0, start))
        g_score: Dict[Tuple[int, int], float] = {vertex: float('inf') for vertex in graph.vertices}
        g_score[start] = 0
        came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
        
        while open_set:
            _, current = heappop(open_set)
            
            if current == end:
                path = []
                while current in came_from:
                    path.insert(0, current)
                    current = came_from[current]
                path.insert(0, start)
                return path, g_score[end]
            
            for neighbor, weight in graph.edges.get(current, {}).items():
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, end)
                    heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current
        
        raise ValueError("Path not found")
    except Exception as e:
        logger.error(f"Error in A* algorithm: {e}")
        raise