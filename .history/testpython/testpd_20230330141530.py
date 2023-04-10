#!/bin/python3
import pandas as pd
import datetime
from string import Template
import sys

def set_df():
    df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})
    return df

df=set_df()
print(df)
df["column_join"]=df["name"]+df["age"].astype(str)

df["column_join2"]="test{}abc".format(df["age"].astype(str))
print(df)

"""
pandasのテスト_
列の値の加工
"""