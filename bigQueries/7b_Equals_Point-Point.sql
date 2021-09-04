-- USE BigBenchmark;

SELECT *
FROM AllNodes as AN1, AllNodes as AN2
WHERE st_equals(AN1.g, AN2.g)