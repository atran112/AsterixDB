Use TinyBenchmark;-- USE TinyBenchmark;

LOAD DATASET RoadNetwork using localfs
(('path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/datasets/OSM2015_road-network.json'),
('format'='adm'));

LOAD DATASET Buildings using localfs
(('path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/datasets/OSM2015_buildings.json'),
('format'='adm'));

LOAD DATASET AllNodes using localfs
(('path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/datasets/OSM2015_all_nodes.json'),
('format'='adm'));

LOAD DATASET TempAllNodes using localfs
(('path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/datasets/OSM2015_all_nodes_SN.json'),
('format'='adm'));

LOAD DATASET TempRoadNetwork using localfs
(('path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/datasets/OSM2015_road-network_SN.json'),
('format'='adm'));