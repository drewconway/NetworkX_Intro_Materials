import networkx as nx

def ego(G,v):
    """Returns Graph of neighbors centered 
    at node n and including n.

    >>> import networkx as nx
    >>> G=nx.star_graph(3)
    >>> G.add_edge(1,10)
    >>> G.add_edge(2,20)
    >>> G.add_edge(3,30)
    >>> E=nx.ego_graph(G,0)
    >>> print E.nodes()
    [0, 1, 2, 3]
    >>> print E.edges()
    [(0, 1), (0, 2), (0, 3)]
    """
    return # E - the ego graph

if __name__=='__main__':
    G=nx.star_graph(3)
    G.add_edges_from([(1,10),(2,20),(3,30)])
    E=ego(G,0)

