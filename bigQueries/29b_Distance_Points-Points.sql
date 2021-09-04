-- USE BigBenchmark;

SELECT AN1.id, COUNT(*) as NearbyNodes
FROM AllNodes AN1, AllNodes AN2
WHERE st_distance(AN1.g, AN2.g) <= 0.017435
GROUP BY AN1.id
ORDER BY NearbyNodes DESC