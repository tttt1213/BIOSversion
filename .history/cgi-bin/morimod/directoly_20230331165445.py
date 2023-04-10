#!/bin/python3
import subprocess

def get_tree(MB):
    cmd = "cd /testDisk;tree -H /testDisk/"+MB
    runcmd = subprocess.call(cmd.split())
    print (runcmd)
    return runcmd
