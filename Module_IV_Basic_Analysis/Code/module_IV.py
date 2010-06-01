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



def main():
	# 1.0 Loading a local data file
	# Load the Hartford drug users data, a directed binary graph.
	# We will specify that the graph be generated as a directed graph, and
	# that the nodes are integers (rather than strings)
	hartford=read_edgelist("../../data/hartford_drug.txt",create_using=DiGraph(),nodetype=int)
	info(hartford)  # Check the the data has been loaded properly

if __name__ == '__main__':
	main()

