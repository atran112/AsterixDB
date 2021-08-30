USE BigBenchmark;

SELECT *
FROM RoadNetwork, Buildings
WHERE st_crosses(RoadNetwork.g, Buildings.g)