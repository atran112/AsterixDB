#!/usr/bin/env python
# coding: utf-8

# In[62]:


import requests
import os
import glob
from natsort import natsorted
import json
import csv
from datetime import datetime
import pandas as pd
import socket


# Test Script

# In[63]:


payload = {'statement': 'select 1;', 'pretty': 'true', 'client_context_id': 'xyz'}
response = requests.get('http://localhost:19002/query/service', params = payload)
response.json()
# row['metrics']['executionTime'] = float(row['metrics']['executionTime'].replace('ms', ''))
# row['metrics']['executionTime']


# In[64]:


isTiny = True

if isTiny:
    dataverse = "USE TinyBenchmark;"
else:
    dataverse = "USE BigBenchmark;"

dataverse += "\n"
print(dataverse)


# In[65]:


cwd = os.getcwd()
cwd += "/"
cwd


# In[66]:


addr = input("Enter address: ")

# print(ip)

downloadsPath = ''

if addr == '127.0.0.1':
    downloadsPath = cwd + "datasets/"
elif addr == '1':
    downloadsPath = "/local_data/downloads/datasets/"
    
print(downloadsPath)


# In[67]:


# path = '/Users/andretran/Documents/Projects/AsterixDB/'
sqlExt = "*.sql"
queriesPath = cwd + "queries/" + sqlExt
print(queriesPath)
tinyQueriesPath = cwd + "tinyQueries/" + sqlExt
bigQueriesPath = cwd + "bigQueries/" + sqlExt

queries = glob.glob(queriesPath)
tinyQueries = glob.glob(tinyQueriesPath)
bigQueries = glob.glob(bigQueriesPath)

if isTiny:
    benchmarkQueries = queries + tinyQueries
else:
    benchmarkQueries = queries + bigQueries

benchmarkQueries = natsorted(benchmarkQueries, key=os.path.basename)
print(benchmarkQueries)


# In[68]:


# Import Module

# Folder Path
# path = "/Users/andretran/Documents/Projects/AsterixDB/queries"

# all_files = glob.glob('/Users/andretran/Documents/Projects/AsterixDB/queries/*.sql')

# Change the directory
os.chdir(cwd)
jsonFile = "tinybenchmark.json"
csvFile = "tinybenchmark.csv"

def create_json_file():
    if os.path.exists(jsonFile):
        os.remove(jsonFile)
        print('JSON file deleted')
    with open(jsonFile, mode='w', encoding='utf-8') as f:
        json.dump([], f)
        print('JSON file created')
        
def create_csv_file():
    if os.path.exists(csvFile):
        os.remove(csvFile)
        print('CSV file deleted')
    with open(csvFile, mode='w', encoding='utf-8') as f:
        header = ['requestID', 'clientContextID', 'status', 'elapsedTime', 'resultCount', 'resultSize', 'processedObjects', 'timestamp']
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        print('CSV file created')
        
create_json_file()
create_csv_file()

def benchmark_queries(file_path, index):
    with open(file_path, 'r') as f:
        statement = f.read()
        if index != 0:
            statement = dataverse + statement
        if index == 22 or 1:
            statement = statement.replace('$PATH$', addr + '://' + downloadsPath)
            
        print(statement)
        payload = {'statement': statement, 'pretty': 'true', 'client_context_id': os.path.basename(file_path), 'readonly': False}
        timestamp = datetime.now()
        response = requests.post('http://localhost:19002/query/service', params = payload)
        row = response.json()
        print(row['status'])
        with open(jsonFile, "r") as of:
            data = json.load(of)
        data.append(row)
        with open(jsonFile, "w") as of:
            json.dump(data, of)
        with open(csvFile, mode='a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([row['requestID'], row['clientContextID'], row['status'], row['metrics']['elapsedTime'], row['metrics']['resultCount'], row['metrics']['resultSize'], row['metrics']['processedObjects'], timestamp])


# iterate through all file
for index, file_path in enumerate(benchmarkQueries):
    # Check whether file is in text format or not
    print(os.path.basename(file_path))
    benchmark_queries(file_path, index)

print("done")


# - uniqueID
# - clientCopntextID as filename
# - check for status if failed or success
# - elapsed time
# - timestamp
# 
# - create sample output file (json and csv)
# 
# - collect memory usage over time (timeseries)
#     - peak memory (how tight a process is in terms of memory comsumption)

# In[ ]:


# statement = "DROP DATAVERSE TinyBenchmark IF EXISTS"
# payload = {'statement': statement, 'pretty': True, 'client_context_id': 'test', 'readonly': False}
# response = requests.post('http://localhost:19002/query/service', params = payload)
# response.json()


# In[14]:


# df = pd.read_csv('tinybenchmark.csv')
# df.dtypes


# In[35]:


# df['elapsedTime'] = df['elapsedTime'].str.replace('ms', '')
# df['elapsedTime'] = df['elapsedTime'].str.replace('s', '')
# df

