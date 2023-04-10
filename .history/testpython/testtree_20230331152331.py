#!/bin/python3
import subprocess

def get_tree(MB):
    cmd = "tree /testDisk/"+MB
    runcmd = subprocess.call(cmd.split())
    print (runcmd)

MB_tree = get_tree("X12SPL-F"")
print(MB_tree)