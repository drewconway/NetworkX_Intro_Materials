#!/usr/bin/env python
# encoding: utf-8
"""
module_II.py

Code in support of Hacking Social Networks with Python
tutorial on NetworkX

Module II - Why do SNA in NetworkX

Created by Drew Conway on 2010-05-24.
Copyright (c) 2010. All rights reserved.
"""

import sys
import os
from networkx import *
import pylab as P

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
    for i in range(len(y_data)):
        if i<2:
            P.text(pos[i]+0.01,y_data[i]+5,int_to_scinot(y_data[i]),color="darkred")
        elif i==2:
            P.text(pos[i]+0.01,y_data[i]+100,int_to_scinot(y_data[i]),color="darkred")
        elif i==3:
            P.text(pos[i]+0.01,y_data[i]+1000,int_to_scinot(y_data[i]),color="darkred")
        elif i==4:
            P.text(pos[i]+0.01,y_data[i]+100000,int_to_scinot(y_data[i]),color="darkred")
        else:
            P.text(pos[i]+0.01,y_data[i]+1000000,int_to_scinot(y_data[i]),color="darkred")
    P.savefig("../../images/figures/net_size_evo.png",dpi=100,format="png")
    
    


def main():
    # Data on the expansion of network data sizes over time
    d=[("Sampson\n(1975)",18),("Zachary\n(1977)",34),("Neural nets\n(1986)",296),("Power grid\n(1998)",4940),("Actor collaboration\n(1999)",212250),("Twitter scrape\n(2008)",2700000)]
    bar_plot_1(d)

if __name__ == '__main__':
    main()

