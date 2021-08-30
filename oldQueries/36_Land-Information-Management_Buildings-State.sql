USE TinyBenchmark;

SELECT States.name, COUNT(*) as TotalBuildings
FROM States, Buildings
WHERE st_contains(States.boundary, Buildings.g)
GROUP BY States.name