import networkx as nx
from typing import *

WHITE = '0'
GRAY = '1'
BLACK = '2'


def top_sort_(graph: nx.DiGraph) -> Tuple(bool, Union[List[str], None]):
    colors = {node: WHITE for node in list(graph.nodes())}
    result = []

    def step(node, graph: nx.DiGraph) -> bool:
        if colors[node] == BLACK:
            return True
        elif colors[node] == GRAY:
            # print('Cycle was found!')
            return False
        colors[node] = GRAY
        for neigbor in graph.neighbors(node):
            res = step(neigbor, graph)
            if not res:
                return False
        colors[node] = BLACK
        result.insert(0, node)
        return True

    for node in list(graph.nodes()):
        res = step(node, graph)
        if not res:
            return False, None

    return True, result
