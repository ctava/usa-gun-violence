# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import time
import requests
import pandas as pd
import numpy as np

raw_data = {'Date': ['12/1/2016', '12/4/2016','12/23/2016', '1/18/2017','1/18/2017','1/19/2017'], 
    'Account': ['aa1', 'aa2','aa1', 'aa1', 'aa1', 'aa2'], 
    'Description': ['store1', 'store2','store1', 'store2','store1','store2' ], 
    'Amount': [26.43, 24.99, 31.54,45.32, 2.00, 15.41],
    'Category': ['G','G','G','G','G','G'],
    'Initials': ['FR','DB','FR','DB','FR','FR']}
df = pd.DataFrame(raw_data, columns = ['Date','Account','Description','Amount','Category','Initials'])
df = df.set_index('Date')

df = df.groupby([pd.TimeGrouper("M"),'Description']).sum().reset_index()
print (df)