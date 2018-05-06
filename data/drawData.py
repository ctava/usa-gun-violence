# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import time
import requests
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()

df3['A'] = pd.Series(list(range(len(df3))))
df3.plot(x='A', y='B')


# Make a square figure and axes
figure(1, figsize=(6, 6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]

explode = (0, 0.05, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Raining Hogs and Dogs', bbox={'facecolor': '0.8', 'pad': 5})

#pylab.savefig('foo.png')


a = np.linspace(0, 10, 100)
b = np.exp(-a)
plt.plot(a, b)
plt.show()