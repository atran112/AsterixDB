USE TinyBenchmark;

SELECT States.name, COUNT(*) as TotalPoints
FROM States, AllNodes
WHERE st_contains(States.boundary, AllNodes.g)
GROUP BY States.name