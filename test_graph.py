# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:04:04 2018

@author: DoW
"""

import pandas as pd
import matplotlib.pyplot as plt

data = [("NONE", "ItemA", "ItemB"), 
        (2013, 100, 50), 
        (2014, 150, 100), 
        (2015, 75, 100),
        (2016, 175, 120),
        (2017, 125, 130),
        (2018, 90, 140)
        ]

df = pd.DataFrame(data)

df1 = pd.DataFrame(data, columns = ["None", "ItemA", "ItemB"])
df2 = df1.drop(0)
df3 = df2.set_index("None")
print(df3)

type(df3["ItemA"])
type(df3["ItemB"])

s1=df3["ItemA"]
ax1=s1.plot()

s2=df3["ItemB"]
ax2=s2.plot()
