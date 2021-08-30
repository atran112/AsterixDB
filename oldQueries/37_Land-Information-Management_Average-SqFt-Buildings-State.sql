USE TinyBenchmark;

SELECT States.name, AVG(st_area(Buildings.g)) as AvgArea
FROM States, Buildings
WHERE st_contains(States.boundary, Buildings.g)
GROUP BY States.name