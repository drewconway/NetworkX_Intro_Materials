import networkx as nx

def degree_centrality(G):

    centrality = {} # empty dictionary
    n=len(G)-1.0 # forces floating point for n
    for v in G:
       centrality[v]=G.degree(v)/n

    return centrality

G=nx.star_graph(3)
dc=degree_centrality(G)
for v in dc:
    print v,dc[v]

print dc
    
