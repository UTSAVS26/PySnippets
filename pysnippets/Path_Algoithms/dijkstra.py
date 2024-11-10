from typing import Tuple, List
from data_classes import Graph
from logger_config import logger

def dijkstra(graph: Graph, start: str, end: str) -> Tuple[List[str], int]:
    try:
        unvisited = {vertex: float('inf') for vertex in graph.vertices}
        unvisited[start] = 0
        visited = {}
        path = {}

        while unvisited:
            current = min(unvisited, key=unvisited.get)
            current_distance = unvisited[current]

            if current == end:
                visited[current] = current_distance
                break

            for neighbor, weight in graph.edges.get(current, {}).items():
                distance = current_distance + weight
                if distance < unvisited.get(neighbor, float('inf')):
                    unvisited[neighbor] = distance
                    path[neighbor] = current

            visited[current] = current_distance
            del unvisited[current]

        if end not in visited or visited[end] == float('inf'):
            raise ValueError("Path not found")

        route = []
        while end:
            route.insert(0, end)
            end = path.get(end)

        return route, visited[route[-1]]
    except Exception as e:
        logger.error(f"Error in Dijkstra's algorithm: {e}")
        raise 