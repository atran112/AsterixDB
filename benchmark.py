#!/usr/bin/env python
# coding: utf-8

# In[114]:


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

# In[115]:


payload = {'statement': 'select 1;', 'pretty': 'true', 'client_context_id': 'xyz'}
response = requests.get('http://localhost:19002/query/service', params = payload)
response.json()
# row['metrics']['executionTime'] = float(row['metrics']['executionTime'].replace('ms', ''))
# row['metrics']['executionTime']


# Ask user for benchmark type (tiny or big)

# In[116]:


benchmarkType = input("Enter tiny for tiny benchmark or large for large benchmark: ")

if benchmarkType == "tiny":
    isTiny = True
elif benchmarkType == "large":
    isTiny = False
else:
    print("Input is invalid. Defaulting to tiny benchmark.")
    benchmarkType = "tiny"
    isTiny = True

if isTiny:
    dataverse = "USE TinyBenchmark;"
else:
    dataverse = "USE BigBenchmark;"

dataverse += "\n"
print(dataverse)


# Check the current working directory

# In[117]:


cwd = os.getcwd()
cwd += "/"
cwd


# Get the path of dataset

# In[118]:


addr = input("Enter address: ")

# print(ip)

datasetsPath = ''

if addr == '127.0.0.1':
    datasetsPath = cwd + "datasets/"
elif addr == '1':
    datasetsPath = "/local_data/downloads/datasets/"
else:
    print("Address is not recognized. Defaulting to 127.0.0.1.")
    addr = '127.0.0.1'
    datasetsPath = cwd + "datasets/"

print(addr)
print(datasetsPath)


# Get the queries based on if the benchmark is tiny or big

# In[119]:


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


# Create a results folder to store benchmark results

# In[131]:


resultsPath = cwd + 'results/'

isExists = os.path.exists(resultsPath)
print(isExists)

if not isExists:
    os.makedirs(resultsPath)
    print("results directory created")
print(resultsPath)


# Create json and csv files which will hold results

# In[122]:


# Import Module

# Folder Path
# path = "/Users/andretran/Documents/Projects/AsterixDB/queries"

# all_files = glob.glob('/Users/andretran/Documents/Projects/AsterixDB/queries/*.sql')

# Change the directory
# os.chdir(resultsPath)
# if os.path.exists(cwd + 'results/'):

dateString = datetime.utcnow().strftime('%Y-%m-%d %H_%M_%S.%f')[:-3]
jsonFile = resultsPath + benchmarkType + "_" + dateString + ".json"
csvFile = resultsPath + benchmarkType + "_" + dateString + ".csv"

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


# Run the benchmark and save results to csv and json files

# In[123]:


def benchmark_queries(file_path, index):
    with open(file_path, 'r') as f:
        statement = f.read()
        if index != 0:
            statement = dataverse + statement
        if index == 22 or 1:
            statement = statement.replace('$PATH$', addr + '://' + datasetsPath)
            
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
