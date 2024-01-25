# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    true_traversal = [
        'Michael Keiser', '33232663', 'Charles Chiu', 'Martin Kampmann', '33242416', 
        '33483487', '32790644', '31806696', '31626775', '31540829', 'Atul Butte', 'Luke Gilbert', 
        'Steven Altschuler', 'Lani Wu', 'Neil Risch', 'Nevan Krogan', '33765435', '31395880', 
        '30944313', '32036252', '32042149', '30727954', '29700475',   '34272374', '32353859',
        'Marina Sirota', 'Hani Goodarzi', 'Michael McManus', '31486345', '32025019'
        ]
    tiny_graph = graph.Graph('data/tiny_network.adjlist')
    empty_graph = graph.Graph('test/blank.adjlist')
    traversal = tiny_graph.bfs('Michael Keiser')
    
    assert len(traversal) == len(true_traversal) and traversal == true_traversal, "Graph traversal is incorrect"

    # Note for BMI 203 graders: 
    # The instructions for this assignment included: "Include a test case that fails and raises an exception."  
    #
    # I wasn't sure if this meant "Include an assertion that causes pytest to fail." or
    # "Include a test case that raises an error which is appropriately handled by pytest." -- I chose the latter.

    with pytest.raises(ValueError, match=r"graph is empty"):
        empty_graph.bfs('Hani Goodarzi')

    with pytest.raises(ValueError, match=r"start node does not exist in graph"):
        tiny_graph.bfs('Sandy Floren')
  

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    citation_graph = graph.Graph('data/citation_network.adjlist')
    shortest_path_bfs = citation_graph.bfs('Hani Goodarzi', 'Atul Butte')
    shortest_path_nx = nx.shortest_path(citation_graph.graph, 'Hani Goodarzi', 'Atul Butte')

    assert len(shortest_path_bfs) == len(shortest_path_nx), "Breadth-first search returns incorrect shortest path"
   
    with pytest.raises(ValueError, match=r"end node does not exist in graph"):
        citation_graph.bfs('Tony Capra', 'Sandy Floren')  

    citation_graph.graph.add_node('Sandy Floren')
    assert citation_graph.bfs('Tony Capra', 'Sandy Floren') is None, 'Breadth-first search did not return None when searching for an unconnected node'
    
