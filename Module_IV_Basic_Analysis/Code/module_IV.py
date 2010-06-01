#!/usr/bin/env python
# encoding: utf-8
"""
module_IV.py

Code in support of Hacking Social Networks with Python
tutorial on NetworkX

Module IV - Basic Analysis

Author:   Drew Conway
Email:    drew.conway@nyu.edu
Date:     2010-06-01

Copyright (c) 2010, under the Simplified BSD License.  
For more information on FreeBSD see: http://www.opensource.org/licenses/bsd-license.php
All rights reserved.
"""

import sys
import os
from networkx import *
from cjson import *
from urllib import *
from time import *
from scipy import array,unique

def snowball_round(G,seeds,myspace=False):
"""Function takes a base graph, and a list of seeds
and builds out the network data by accessing the
Google SocialGraph API."""
    t0=time()
    if myspace:
        seeds=get_myspace_url(seeds)
    sb_data=[]
    for s in range(0,len(seeds)):
        s_sg=get_sg(seeds[s])
        new_ego,pen=create_egonet(s_sg) # Create ego net of seed
        # Compose new network data into old abse graph
        for p in pen:
                sb_data.append(p)
        if s<1:
            sb_net=compose(G,new_ego)
        else:
            sb_net=compose(new_ego,sb_net)
        del new_ego
        if s==round(len(seeds)*0.2):
        # Simple progress output, useful for long jobs
            sb_net.name='20% complete'
            info(sb_net)
            print 'AT: '+strftime('%m/%d/%Y, %H:%M:%S', gmtime())
            print ''
        if s==round(len(seeds)*0.4):
            sb_net.name='40% complete'
            info(sb_net)
            print 'AT: '+strftime('%m/%d/%Y, %H:%M:%S', gmtime())
            print ''
        if s==round(len(seeds)*0.6):
            sb_net.name='60% complete'
            info(sb_net)
            print 'AT: '+strftime('%m/%d/%Y, %H:%M:%S', gmtime())
            print ''
        if s==round(len(seeds)*0.8):
            sb_net.name='80% complete'
            info(sb_net)
            print 'AT: '+strftime('%m/%d/%Y, %H:%M:%S', gmtime())
            print ''
        if s==len(seeds)-1:
            print 'NEW NETWORK COMPLETE!'
            print 'AT: '+strftime('%m/%d/%Y, %H:%M:%S', gmtime())
            sb_net.name=G.name+'--> '
    # Return newly discovered seeds
    sb_data=array(sb_data)
    sb_data.flatten()
    sb_data=unique(sb_data)
    info(sb_net)
    return sb_net,sb_data
        
def get_myspace_url(seeds):
"""Special function for parsing myspace.com users"""
    uids=[]
    for s in seeds:
        b=s.split('=')
        b=b[len(b)-1]
        uids.append('http://www.myspace.com/'+str(b))
    return uids

def create_egonet(s):
"""Base function for creating an ego network from some 
SocialGraph URL"""
    try:
        raw=decode(s)
        G=DiGraph()
        pendants=[]
        n=raw['nodes']
        nk=n.keys()
        G.name=str(nk)
        pendants=[]
        # We simply add edges iteratively
        for a in range(0,len(nk)):
            for b in range(0,len(nk)):
                if a!=b:
                    G.add_edge(nk[a],nk[b])
        for k in nk:
            ego=n[k]
            # Access the appropriate JSON datum for in- and out-degrees
            ego_out=ego['nodes_referenced']     
            for o in ego_out:
                G.add_edge(k,o)
                pendants.append(o)
            ego_in=ego['nodes_referenced_by']
            for i in ego_in:
                G.add_edge(i,k)
                pendants.append(i)
        pendants=array(pendants,dtype=str)
        pendants.flatten()
        pendants=unique(pendants)
        return G,pendants
    except DecodeError:
        print 'WEB ERROR--Returning empty DiGraph'
        G=DiGraph()
        pendants=[]
        return G,pendants
    except KeyError:
        print 'NET BUILD ERROR FOR: '+str(nk)+'--Returning empty DiGraph'
        G=DiGraph()
        pendants=[]
        return G,pendants

def get_sg(seed_url):
"""Create Internet socket for some seed URL"""
    sgapi_url="http://socialgraph.apis.google.com/lookup?q="+seed_url+"&edo=1&edi=1&fme=1&pretty=0"
    try:
        furl=urlopen(sgapi_url)
        fr=furl.read()
        furl.close()
        return fr
    except IOError:
        print "Could not connect to website"
        print sgapi_url
        return {}



def main():
	# 1.0 Loading a local data file
	# Load the Hartford drug users data, a directed binary graph.
	# We will specify that the graph be generated as a directed graph, and
	# that the nodes are integers (rather than strings)
	hartford=read_edgelist("../../data/hartford_drug.txt",create_using=DiGraph(),nodetype=int)
	info(hartford)  # Check the the data has been loaded properly
	
	# 2.0 Connecting to a database
	
	# 3.0 Building a network directly from the Internet
    seed="imichaeldotorg"   # Set the seed user within livejournal.com
    seed_url="http://"+seed+".livejournal.com"
    # 3.1 Scrape, parse and build seed's ego net
    sg=get_sg(seed_url)
    net,newnodes=create_egonet(sg)
    write_pajek(net,"seed_ego.net") # Save data as Pajek
    info(net)
    # 3.2 Perform snowball search, where k=2
    k=2
    for g in range(k):
        net,newnodes=snowball_round(net,newnodes)
        write_pajek(net,seed+"_step_"+str(g+1)+".net")
    
if __name__ == '__main__':
	main()

