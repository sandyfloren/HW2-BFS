import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        Perform a breadth first traversal and pathfinding on the graph.

        * If there's no end node input, return a list of nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # This implementation of BFS uses a queue of (node, path) tuples in order to keep track of the paths from the
        # start node to each node visited by the graph.

        # Check if the graph is empty.
        if not list(self.graph.nodes()):
            raise ValueError("graph is empty")
        # Check if start node exists in the graph. 
        if start not in list(self.graph.nodes()):
            raise ValueError("start node does not exist in graph")
        # Check if end node exists in the graph.
        if end:
            if end not in list(self.graph.nodes()):
                raise ValueError("end node does not exist in graph")
        # Check if start node and end node are equal.
        if start == end:
            return [start]
        
        # Initialize list of visited nodes and queue of (node, path) tuples.
        visited = [start] 
        frontier = deque([(start, [start])])

        # Run BFS.
        while frontier:
            node, path = frontier.popleft()
            # If end node is found, return shortest path.          
            if node == end:
                return path
            for v in self.graph.adj[node]:
                if v not in visited:
                    visited.append(v)
                    frontier.append((v, path + [v]))      

        # If end node was specified but not found, return None.
        if end:
            return None
        # If end node was not specified, return list of nodes in order of traversal.
        else:
            return visited