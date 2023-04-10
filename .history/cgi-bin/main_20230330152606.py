#!/bin/python3
import pandas as pd
import datetime
from string import Template
import sys
import cgi
form = cgi.FieldStorage()
from morimod import moripri

print("Content-Type: text/plain\n")
print('Hello, World!')