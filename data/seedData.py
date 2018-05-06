# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import time
import requests
import pandas as pd
import numpy as np

#Variables
hostname = 'https://usa-gun-violence.appspot.com'
#hostname = 'http://localhost:8080'
endpoint = '/data'

#Functions
def putItem(hostName,endpoint,df):
    df['year'] = df['date'].strftime('%Y')
    df['month'] = df['date'].strftime('%m')
    payload = 'incidentID='+str(df.incident_id)+'&year='+df.year+'&month='+df.month+'&state='+str(df.state)+'&city_or_county='+str(df.city_or_county)+'&n_killed='+str(df.n_killed)+'&n_injured='+str(df.n_injured)+'&latitude='+str(df.latitude)+'&longitude='+str(df.longitude)
    r = requests.put(hostName+endpoint, params=payload)
    print df.incident_id, r.text

#Main Script
print "Start"        
beginTime = time.time();  

dfs = pd.read_csv('data.csv',skiprows=0,parse_dates=['date'])
for index, row in dfs.iterrows():
    putItem(hostname,endpoint,row)

endTime = time.time();
print "End"
print endTime - beginTime , "secs to put data into the cloud." 