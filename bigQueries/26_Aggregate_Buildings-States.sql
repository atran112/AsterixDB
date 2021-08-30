USE BigBenchmark;

SELECT States.name, SUM(st_area(Buildings.g)) as TotalArea
FROM States, Buildings
WHERE st_contains(States.g, Buildings.g)
GROUP BY States.name