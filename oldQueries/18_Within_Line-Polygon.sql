USE BigBenchmark;

SELECT *
FROM RoadNetwork, Buildings
WHERE st_within(RoadNetwork.g, Buildings.g)