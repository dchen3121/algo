# Given an undirected graph with maximum degree D, find a graph coloring using at most D+1 colors.

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

# Example graph:
# a -- b -- c

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]


from typing import List, Set


def graph_colouring(graph: List[GraphNode], colors: Set[int]) -> None:
    for node in graph:
        if node in node.neighbours:
            raise Exception
        illegal_colors = { neighbor.color for neighbor in node.neighbors if neighbor.color }
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break
        if not node.color:
            raise Exception

