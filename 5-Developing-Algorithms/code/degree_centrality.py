import networkx as nx

def degree_centrality(G):

    n=len(G)-1.0 # forces floating point for n
    for v in G:
        print v,G.degree(v)/n

    return

G=nx.star_graph(3)
degree_centrality(G)

#if __name__='__main__':
    
