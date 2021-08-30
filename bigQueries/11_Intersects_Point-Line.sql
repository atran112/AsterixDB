USE BigBenchmark;

SELECT *
FROM AllNodes, RoadNetwork
WHERE st_intersects(AllNodes.g, RoadNetwork.g)