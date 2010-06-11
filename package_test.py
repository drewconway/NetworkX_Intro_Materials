#!/usr/bin/env python
# encoding: utf-8
"""
package_test.py

Purpose:    Test script to make sure all required packages are installed
for Sunbelt XXX workshop

Author:   Drew Conway
Email:    drew.conway@nyu.edu
Date:     2010-06-11

Copyright (c) 2010, under the Simplified BSD License.  
For more information on FreeBSD see: http://www.opensource.org/licenses/bsd-license.php
All rights reserved.
"""

import sys
import os

def test_packs(pack_list):
    """Tests to make sure you have all software for
    NetworkX workshop"""
    missing=list()
    for p in pack_list:
        try:
            exec("import "+p+" as T")
            ver=T.__version__
            print "You have "+p+" version "+ver+" installed!"
        except ImportError:
            missing.append(p)
    print ""
    if len(missing)<1:
        print "#########  YOU HAVE ALL PACKAGES INSTALLED! ######### "
    else:
        print "#########    YOU ARE MISSING THE FOLLOWING PACKAGES    #########"
        for m in missing:
            print m
        
            
def main():
    # PACKAGES
    packs=['networkx','matplotlib','numpy','scipy','pygraphviz','nose','cjson']
    # TEST PACK INSTALLATION
    test_packs(packs)

if __name__ == '__main__':
    main()

