![BuildStatus](https://github.com/sandyfloren/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)
# Assignment 2
Breadth-first search (BFS)

# BFS overview
Given a directed, unweighted graph $G$, and a start node $u$, do one of the following:
* If an end node $v$ is given, perform BFS and return the shortest path in $G$ between $u$ and $v$. 
* If an end node $v$ is given, but there is no path in $G$ from $u$ to $v$, return `None`.
* If no end node is given, return a list of all nodes in $G$ reachable from $u$ in the order visited by BFS.

This implementation of BFS uses a queue of (node, path) tuples, where path is a list of nodes in order to keep track of the paths from the start node to each node visited by the graph.