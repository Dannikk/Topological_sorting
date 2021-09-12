import os
import networkx as nx


DELIMITER = ':'
NODES_DELIMITER = ','


def read_graph(file_path: str):
    """
    Function that reads a graph from a text file
    Parameters
    ----------
    file_path : str
        directory to file to read graph
    Returns
    -------
    generator :
        yielding node (any hashable object), list of neighbors
    """
    with open(file_path, 'r') as file:
        for line in file:
            node, _, neighbors = line.partition(DELIMITER)
            assert neighbors
            yield node, neighbors.replace(NODES_DELIMITER, '').split()


def graph_builder(file_path: str) -> nx.DiGraph:
    """
    Function that construct networkx.Graph using generator
    Parameters
    ----------
    file_path : str
        directory to file to read graph
    Returns
    -------
    `~networkx.Graph` :
        graph constructing from the text file located in file_path
    """
    graph = nx.DiGraph()
    for nod, neighs in read_graph(file_path):
        for neighbour in neighs:
            graph.add_edge(nod, neighbour)
    return graph