#!/usr/bin/env python
# encoding: utf-8
"""
add_data.py

Script to add network data to public MySQL database

Created by Drew Conway on 2010-05-25.
Copyright (c) 2010. All rights reserved.
"""

import sys
import os
from MySQLdb import *


def main():
    file_path="../../data/www.txt"
    db=MySQLdb.connect(user="guest",passwd="networks",db="sunbelt_public",host="www.freesql.org",port="3306")


if __name__ == '__main__':
    main()

