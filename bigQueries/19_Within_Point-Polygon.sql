USE BigBenchmark;

SELECT *
FROM AllNodes, Buildings
WHERE st_within(AllNodes.g, Buildings.g)