#!/bin/python3
"""
from morimod import directory

#tree = directory.get_tree("X12STL-F")
#print (tree)

path = directory.get_path('X12STL-F')
print(path)
"""
from morimod import directory2

tree = directory2.TDtree()
tree.setMB("X12SPL-F")
print(tree.getMB())