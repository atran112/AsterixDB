USE BigBenchmark;

SELECT *
FROM Buildings as B1, Buildings as B2
WHERE st_overlaps(B1.g, B2.g)