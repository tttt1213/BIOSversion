#!/bin/python3
import subprocess

def get_tree(MB):
    cmd = "tree  /testDisk/"+MB
    runcmd = subprocess.call(cmd.split())

    return runcmd
