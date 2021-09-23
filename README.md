# Benchmark
This repository includes all necessary items to benchmark query performance with AsterixDB. The folders/files are listed below:
1. **datasets:** contains datasets that will be used in our benchmark. The use of the datasets will depend on which benchmark type is used (tiny or big).
2. **queries:** contains queries that will run in both the tiny benchmark and large benchmark. There are 31 out of 37 total queries in this folder. The remaining 6 queries will be based on the benchmark type (tiny or big).
3. **bigQueries:** contains 6 queries that are specific to the big benchmark. These queries are denoted by a "b" in the filename.
4. **tinyQueries:** contains 6 queries that are specific to the tiny benchmark. These queries are denoted by an "a" in the filename.
5. **oldQueries:** contains queries that will no longer be used due to various reasons and will not be used in the benchmark.
6. **PostGIS** contains queries that could be used for a PostGIS benchmark. However, some of the the queries are incomplete and/or may need to be reevaluated. These queries will not be used in the benchmark. These queries are denoted by a "c" in the benchmark.
7. **results:** contains the results of the benchmark in csv and json format.
8. **benchmark.ipynb:** a notebook containing the benchmark
9. **benchmark.py:** a python script (derived from the notebook) that will be used to benchmark the performance of AsterixDB.

## How to Run

Do the following before running the program:
1. Start AsterixDB cluster
2. Install python3
3. Install all libraries in the import section of the script

We will convert our notebook to a python file to ensure our script is up to date. Do the following:
```bash
jupyter nbconvert --to script benchmark.ipynb
```

Now, we can run the benchmark using python3 by doing the following:

```bash
python3 benchmark.py
```
## Inputs
The program will ask for input when running:
1. Enter tiny for tiny benchmark or big for big benchmark: 
    - The input will determine whether to run the tiny or big version of the benchmark. Thus, the program will either use queries in the folder "tinyQueries" or "bigQueries".
    - Queries found in the folder "queries" will be used regardless of benchmark type
    - If input is invalid, it will default to "tiny"

2. Enter address:
    - The input will determine the address of the computer you are using
    - Currently the prompt will only accept either '127.0.0.1' or '1'. If the input is invalid it will default to the former.
    - If you are using your local machine use '127.0.0.1'. If you are running on a cluster, use '1'.

The program will now run 37 queries and will save the results.

## Output
While the program is running, the results of the benchmark will be saved to the "results" folder. Two files will be created - one of type csv and the other of type json. The file names will follow the format of benchmark type, datetime, then file type. For example, a file name could be "tiny_2021-09-07 07_23_32.015.csv". CSV contains more curated information (clientContextID, status, elapsedTime, etc.) for data analysis, while JSON contains everything in CSV in addition to the actual query results.