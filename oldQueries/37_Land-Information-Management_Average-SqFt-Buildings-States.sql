USE BigBenchmark;

SELECT States.name, AVG(st_area(Buildings.g)) as AvgArea
FROM States, Buildings
WHERE st_contains(States.g, Buildings.g)
GROUP BY States.name