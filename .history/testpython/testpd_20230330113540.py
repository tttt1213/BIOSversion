#!/bin/python3
import pandas as pd
import datetime
from string import Template
import sys

now_df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})