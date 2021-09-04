USE BigBenchmark;

SELECT States.name, COUNT(*) as TotalPoints
FROM States, AllNodes
WHERE st_contains(States.g, AllNodes.g)
GROUP BY States.name