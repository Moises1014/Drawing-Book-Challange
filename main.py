#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    min_from_1 = 0
    min_from_last_page =0 
    if(p<=n):
        #turn to page from first page
        #divede total page or n by 2 since to per page
        min_from_1 = p//2
        #turn to page from last page
        #since the n(number of page) would be smaller than pages in book
        min_from_last_page = n//2 - p//2
        #python function to get minimum to return smaller between the two
        return min(min_from_1,min_from_last_page)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    p = int(raw_input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
