# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import time
import requests
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

#Variables
hostname = 'https://usa-gun-violence.appspot.com'
#hostname = 'http://localhost:8080'
#endpoint = '/data'
endpoint = '/yearsummary'

#Functions
def processRow(df):
    df['year'] = df['date'].strftime('%Y')
    df['month'] = df['date'].strftime('%m')
    #payload = 'incidentID='+str(df.incident_id)+'&year='+df.year+'&month='+df.month+'&state='+str(df.state)+'&city_or_county='+str(df.city_or_county)+'&n_killed='+str(df.n_killed)+'&n_injured='+str(df.n_injured)+'&latitude='+str(df.latitude)+'&longitude='+str(df.longitude)
    print df['year'], df['month'], df.n_injured, df.n_killed

def putIncident(hostName,endpoint,df):
    df['year'] = df['date'].strftime('%Y')
    df['month'] = df['date'].strftime('%m')
    payload = 'incidentID='+str(df.incident_id)+'&year='+df.year+'&month='+df.month+'&state='+str(df.state)+'&city_or_county='+str(df.city_or_county)+'&n_killed='+str(df.n_killed)+'&n_injured='+str(df.n_injured)+'&latitude='+str(df.latitude)+'&longitude='+str(df.longitude)
    r = requests.put(hostName+endpoint, params=payload)
    print df.incident_id, r.text

def putYearSummary(hostName,endpoint,year):
    columns = ['year','month','n_injured','n_killed']
    indexes = []
    lst = []
    for i in range(13):
        if i == 0: 
            continue
        month = str(i).zfill(2)
        lst.append([year,month,0,0])
    dfSUM = pd.DataFrame(data=lst,columns=columns)
    #dfSUM[['n_injured', 'n_killed']] = dfSUM[['n_injured', 'n_killed']].astype(int)
    dfData = pd.read_csv(str(year)+'.csv',skiprows=0, parse_dates=['date'])
    #dfData[['n_injured', 'n_killed']] = dfData[['n_injured', 'n_killed']].astype(int)
    #dfData = dfData.infer_objects()
    for index, row in dfData.iterrows():
        row['month'] = row['date'].strftime('%m')
        df = dfSUM.loc[dfSUM['month'] == row['month']]
        df['n_injured'] = df['n_injured'] + row['n_injured']
        df['n_killed'] = df['n_killed'] + row['n_killed']
        dfSUM.update(df)
    for index, row in dfSUM.iterrows():
        payload = 'year='+str(row.year).rstrip('.0')+'&month='+str(row.month)+'&n_killed='+str(row.n_killed).rstrip('.00')+'&n_injured='+str(row.n_injured).rstrip('.00')
        r = requests.put(hostName+endpoint, params=payload)
        print row.year, row.month, r.text

def putYearSummaryByMonth(hostName,endpoint,year):
    columns = ['year','month','n_injured','n_killed']
    indexes = []
    lst = []
    for i in range(13):
        if i == 0: 
            continue
        month = str(i).zfill(2)
        lst.append([year,month,0,0])
    dfSUM = pd.DataFrame(data=lst,columns=columns)

    for i in range(13):
        if i == 0: 
            continue
        month = str(i).zfill(2)
        dfMonth = pd.read_csv(str(year)+"-"+str(month)+'.csv',skiprows=0, parse_dates=['date'])
        dfMonth['month'] = dfMonth['date'].dt.strftime('%m')
        #dfMonth.set_index('month',drop=False)
        for index, row in dfMonth.iterrows():
            #row['month'] = row['date'].strftime('%m')
            dfSumRec = dfSUM.loc[dfSUM['month'] == row['month']]
            dfSumRec['n_injured'] = dfSumRec['n_injured'] + row['n_injured']
            dfSumRec['n_killed'] = dfSumRec['n_killed'] + row['n_killed']
            dfSUM.update(dfSumRec)
    for index, row in dfSUM.iterrows():
        payload = 'year='+str(row.year).rstrip('.0')+'&month='+str(row.month)+'&n_killed='+str(row.n_killed).rstrip('.00')+'&n_injured='+str(row.n_injured).rstrip('.00')
        r = requests.put(hostName+endpoint, params=payload)
        print row.year, row.month, r.text

def prepData(year):
    dfYear = pd.read_csv(str(year)+'.csv',skiprows=0, parse_dates=['date'])
    dfYear['month'] = dfYear['date'].dt.strftime('%m')
    for i in range(13):
        if i == 0: 
            continue
        month = str(i).zfill(2)
        dfMonth = dfYear[dfYear['month'] == month]
        dfMonth.to_csv(str(year)+"-"+str(month)+".csv")

#Main Script
print "Start"        
beginTime = time.time();  

year = 2013
#prepData(year)
putYearSummary(hostname,endpoint,year)
#putYearSummaryByMonth(hostname,endpoint,year)

'''
year = 2014
prepData(year)

year = 2015
prepData(year)

year = 2016
prepData(year)

year = 2017
prepData(year)

year = 2018
prepData(year)

#putYearSummaryByMonth(hostname,endpoint,year)


year = 2015
putYearSummary(hostname,endpoint,year)

year = 2016
putYearSummary(hostname,endpoint,year)

year = 2017
putYearSummary(hostname,endpoint,year)

year = 2018
putYearSummary(hostname,endpoint,year)'''

"""
for index, row in df.iterrows():
    dfSum['month'] = row['date'].strftime('%m')

print("2013:",df['month,n_injured'].sum(),df['monthn_killed'].sum())

df2014 = pd.read_csv('2014.csv',skiprows=0, parse_dates=['date'])
for index, row in df2014.iterrows():
    putYearSummary(hostname,endpoint,row)
print("2014:",df2014['n_injured'].sum(),df2014['n_killed'].sum())

df2015 = pd.read_csv('2015.csv',skiprows=0, parse_dates=['date'])
for index, row in df2015.iterrows():
    putYearSummary(hostname,endpoint,row)
print("2015:",df2015['n_injured'].sum(),df2015['n_killed'].sum())

df2016 = pd.read_csv('2016.csv',skiprows=0, parse_dates=['date'])
for index, row in df2016.iterrows():
    putYearSummary(hostname,endpoint,row)
print("2016:",df2016['n_injured'].sum(),df2016['n_killed'].sum())

df2017 = pd.read_csv('2017.csv',skiprows=0, parse_dates=['date'])
for index, row in df2017.iterrows():
    putYearSummary(hostname,endpoint,row)
print("2017:",df2017['n_injured'].sum(),df2017['n_killed'].sum())

df2018 = pd.read_csv('2018.csv',skiprows=0, parse_dates=['date'])
for index, row in df2018.iterrows():
    putYearSummary(hostname,endpoint,row)
print("2018:",df2018['n_injured'].sum(),df2018['n_killed'].sum())
"""
#df2013 = dfs[dfs['date'].dt.year == 2013]
#df2014 = dfs[dfs['date'].dt.year == 2014]
#df2015 = dfs[dfs['date'].dt.year == 2015]
#df2016 = dfs[dfs['date'].dt.year == 2016]
#df2017 = dfs[dfs['date'].dt.year == 2017]
#df2018 = dfs[dfs['date'].dt.year == 2018]
#print("2013:",dfs['n_injured'].sum(),dfs['n_killed'].sum())
#print("2013:",df2013['n_injured'].sum(),df2014['n_killed'].sum())
#print("2014:",df2014['n_injured'].sum(),df2014['n_killed'].sum())
#print("2015:",df2015['n_injured'].sum(),df2015['n_killed'].sum())
#print("2016:",df2016['n_injured'].sum(),df2016['n_killed'].sum())
#print("2017:",df2017['n_injured'].sum(),df2017['n_killed'].sum())
#print("2018:",df2018['n_injured'].sum(),df2018['n_killed'].sum())
#df2013.to_csv("2013.csv")
#df2014.to_csv("2014.csv")
#df2015.to_csv("2015.csv")
#df2016.to_csv("2016.csv")
#df2017.to_csv("2017.csv")
#df2018.to_csv("2018.csv")

#df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))

#df = df.cumsum()

#plt.figure(); df.plot();

endTime = time.time();
print "End"
print endTime - beginTime , "secs to put data into the cloud." 
