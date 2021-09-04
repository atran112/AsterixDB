-- USE TinyBenchmark;

SELECT *
FROM TempAllNodes, TempRoadNetwork
WHERE st_intersects(TempAllNodes.g, TempRoadNetwork.g)