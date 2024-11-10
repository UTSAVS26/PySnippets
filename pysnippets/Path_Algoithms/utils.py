from data_classes import Graph
from logger_config import logger
from typing import List, Dict

def create_graph(vertices: List[str], edges: Dict[str, Dict[str, int]]) -> Graph:
    try:
        graph = Graph(vertices=vertices, edges=edges)
        logger.debug("Graph created successfully")
        return graph
    except Exception as e:
        logger.error(f"Error creating graph: {e}")
        raise 