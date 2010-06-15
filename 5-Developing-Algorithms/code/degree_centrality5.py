def degree_centrality(G):
    return dict((n,d/(len(G)-1.0)) for n,d in G.degree_iter())


