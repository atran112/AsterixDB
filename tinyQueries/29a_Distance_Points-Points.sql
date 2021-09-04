-- USE TinyBenchmark;

SELECT TAN1.id, COUNT(*) as NearbyNodes
FROM TempAllNodes TAN1, TempAllNodes TAN2
WHERE st_distance(TAN1.g, TAN2.g) <= 0.017435
GROUP BY TAN1.id
ORDER BY NearbyNodes DESC