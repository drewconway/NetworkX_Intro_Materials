#!/usr/bin/env python
# encoding: utf-8
"""
module_II.py

Code in support of Hacking Social Networks with Python
tutorial on NetworkX

Module II - Why do SNA in NetworkX

Created by Drew Conway on 2010-05-24.
Copyright (c) 2010, under the General Purpose License (GPL) v3.
For more information on GPLv3 see: http://www.gnu.org/licenses/gpl.html
All rights reserved.
"""

import sys
import os
from networkx import *
import pylab as P
from datetime import datetime
from numpy import random

def int_to_scinot(x):
    """Take an integer and convert to text in scietification notation"""
    int_len=len(str(x))-1
    x=float(x)
    x=round(x*10**-(int_len),2)
    return str(x)+"*10^"+str(int_len)
    

def bar_plot_1(data):
    """Generates bar plot from data"""
    x_labels=[a for (a,b) in data]
    y_data=[b for (a,b) in data]
    # Create chart
    pos=range(1,len(x_labels)+1)
    P.figure(1,figsize=(11,7))
    P.bar(left=pos,height=y_data,log=True,width=.6,color="lightgrey",edgecolor="indigo")
    pos2=[a+.3 for a in pos]
    P.xticks(pos2,x_labels)
    P.title("Evolution of network data size over time",fontsize="x-large")
    P.xlabel("Network data sets (year published)",fontsize="large")
    P.ylabel("Number of vertices [log(N)]",fontsize="large")
    text_color="black"
    for i in range(len(y_data)):
        if i<2:
            P.text(pos[i]+0.01,y_data[i]+5,int_to_scinot(y_data[i]),color=text_color)
        elif i==2:
            P.text(pos[i]+0.01,y_data[i]+100,int_to_scinot(y_data[i]),color=text_color)
        elif i==3:
            P.text(pos[i]+0.01,y_data[i]+1000,int_to_scinot(y_data[i]),color=text_color)
        elif i==4:
            P.text(pos[i]+0.01,y_data[i]+100000,int_to_scinot(y_data[i]),color=text_color)
        else:
            P.text(pos[i]+0.01,y_data[i]+1000000,int_to_scinot(y_data[i]),color=text_color)
    P.savefig("../../images/figures/net_size_evo.png",dpi=100,format="png")
    
    
def time_series(num_nodes,p):
    """Creates a random network (Erdos-Renyi) where nodes are time-stamps for when the
    node was created, and edges are time-stamps for when the edge was created
    
    num_nodes:  Number of nodes in graph
    p:          Probability of edge between nodes
    """
    if p>=0 and p<=1:
        G=DiGraph()
        # Create datetime object nodes
        for v in xrange(num_nodes):
            G.add_node(datetime.now())
        time_nodes=G.nodes()
        # Add edges with 'time' attribute
        for i in xrange(num_nodes):
            draws=random.uniform(0,1,num_nodes)
            for j in xrange(num_nodes):
                if i!=j and draws[j]<=p:
                    G.add_edge(time_nodes[i],time_nodes[j],time=datetime.now())
        return G
    else:
        raise ValueError("p must be between 0 and 1")
        
        
def main():
    # 1.0 Data on the expansion of network data sizes over time
    d=[("Sampson\n(1975)",18),("Zachary\n(1977)",34),("Neural nets\n(1986)",296),("Power grid\n(1998)",4940),("Actor collaboration\n(1999)",212250),("Twitter scrape\n(2008)",2700000)]
    bar_plot_1(d)
    
    # 2.0 Create NetowrkX objects with time-series data
    g1=time_series(100,.25)
    write_edgelist(g1,'../../data/time_series.txt',data=True)

    # 3.0 Load Sampson monastery data and output as DOT
    g2=read_edgelist("../../data/samp_like_el.txt",delimiter="\t",create_using=DiGraph())
    info(g2)
    # Convert to pygraphviz type
    g2_gv=to_agraph(g2)
    # Output DOT file and draw using dot layout
    g2_gv.write("../../data/samp_like_dot.dot")
    g2_gv.draw('../../images/networks/samp_like.png',prog='dot')
    
if __name__ == '__main__':
    main()

