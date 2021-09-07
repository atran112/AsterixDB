-- USE TinyBenchmark;

-- 'path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/datasets/OSM2015_road-network.json'

LOAD DATASET RoadNetwork using localfs
(('path'= '$PATH$OSM2015_road-network.json'),
('format'='adm'));

LOAD DATASET Buildings using localfs
(('path'= '$PATH$OSM2015_buildings.json'),
('format'='adm'));

LOAD DATASET AllNodes using localfs
(('path'= '$PATH$OSM2015_all_nodes.json'),
('format'='adm'));

LOAD DATASET TempAllNodes using localfs
(('path'= '$PATH$OSM2015_all_nodes_SN.json'),
('format'='adm'));

LOAD DATASET TempRoadNetwork using localfs
(('path'= '$PATH$OSM2015_road-network_SN.json'),
('format'='adm'));