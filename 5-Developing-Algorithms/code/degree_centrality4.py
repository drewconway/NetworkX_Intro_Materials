def degree_centrality(G):
    """Compute degree centrality for nodes.

    The degree centrality for a node is the fraction of all other
    nodes it is connected to.

    >>> import networkx as nx
    >>> G=nx.star_graph(3)
    >>> print degree_centrality(G)[0]
    1.0
    """
    centrality = {} # empty dictionary
    n=len(G)-1.0 # forces floating point for n
    for v in G:
       centrality[v]=G.degree(v)/n
    return centrality

if __name__=='__main__':
    import networkx as nx
    G=nx.star_graph(3)
    for v,c in degree_centrality(G).items():
        print v,c
    
