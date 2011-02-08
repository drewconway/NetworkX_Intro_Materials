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
required={'networkx':'1.1',
          'matplotlib':'0.99.0',
          'numpy':'1.3.0',
          'scipy':'0.7.0'}

optional={'nose':'0.11.1',
          'pyparsing':'1.5.0',
          'pydot':'1.0.2',
          'foo':'1.0'}

def test_packs(package_list):
    """Tests to make sure you have all software for NetworkX workshop"""
    for p,v in package_list.items():
        try:
            exec("import "+p+" as T")
            ver=T.__version__
            want=v.split('.')
            need=ver.split('.')
            versionok=True
            for w,n in zip(want,need):
                if w.isdigit() and n.isdigit():
                    if int(w)>int(n):
                        versionok=False
            if versionok:
                print "%12s-%-8s [installed] version [OK] %s"%(p,v,ver)
            else:
                print "%12s-%-8s [installed] version [NOTOK] %s"%(p,v,ver)

        except ImportError:
            print "%12s-%-8s [missing]"%(p,v)
            install=raw_input("Attmpt to install? [y/n]: ")
            if(install.lower()=="y"):
                exec("easy_install "+p)
        
if __name__ == '__main__':
    print "Required"
    print "--------"
    test_packs(required)
    print
    print "Optional"
    print "--------"
    test_packs(optional)


