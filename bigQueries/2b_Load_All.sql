-- USE BigBenchmark;

LOAD DATASET RoadNetwork using localfs
(('path'='$PATH$OSM2015_road-network.json'),
('format'='adm'));

LOAD DATASET Buildings using localfs
(('path'='$PATH$OSM2015_buildings.json'),
('format'='adm'));

LOAD DATASET AllNodes using localfs
(('path'='$PATH$OSM2015_all_nodes.json'),
('format'='adm'));