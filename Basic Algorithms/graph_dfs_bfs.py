from typing import List, Set
from collections import deque


class Graph:
    def __init__(self) -> None:
        self.nodes = set()
        self.adjacency_list = dict()

    def add_edge(self, node_1: str, node_2: str) -> None:
        if node_1 not in self.nodes:
            self.nodes.add(node_1)
            self.adjacency_list[node_1] = set()
        if node_2 not in self.nodes:
            self.nodes.add(node_2)
            self.adjacency_list[node_2] = set()
        self.adjacency_list[node_1].add(node_2)
        self.adjacency_list[node_2].add(node_1)

    def neighbours(self, node: str) -> Set[str]:
        if node in self.nodes:
            return self.adjacency_list[node]
        return set()

    def populate_sample_graph(self) -> None:
        self.nodes = ['Anne', 'Bob', 'Chris', 'Deb', 'Ein']
        self.adjacency_list = {
            'Anne': {'Bob', 'Deb'},
            'Bob': {'Anne', 'Chris', 'Ein'},
            'Chris': {'Bob', 'Deb', 'Ein'},
            'Deb': {'Anne', 'Chris'},
            'Ein': {'Bob', 'Chris'},
        }

    def dfs(self, node) -> List[str]:
        if node not in self.nodes:
            return []

        visited = {node}
        stack = [node]
        result = []

        while stack:
            curr_node = stack.pop()
            result.append(curr_node)
            for neighbour in self.neighbours(curr_node):
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return result

    def bfs(self, node) -> List[str]:
        if node not in self.nodes:
            return []

        visited = {node}
        queue = deque()
        queue.append(node)
        result = []

        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for neighbour in self.neighbours(curr_node):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return result

graph = Graph()
graph.populate_sample_graph()
print(graph.dfs('Anne'))
print(graph.bfs('Anne'))
