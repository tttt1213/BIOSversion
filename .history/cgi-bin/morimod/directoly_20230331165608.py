#!/bin/python3
import subprocess

def get_tree(MB):
    cmd = "tree  /testDisk -H /testDisk/"+MB
    runcmd = subprocess.call(cmd.split())
    print (runcmd)
    return runcmd
