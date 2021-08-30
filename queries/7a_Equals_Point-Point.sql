-- USE TinyBenchmark;

SELECT *
FROM TempAllNodes as TAN1, TempAllNodes as TAN2
WHERE st_equals(TAN1.g, TAN2.g)