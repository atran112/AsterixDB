USE BigBenchmark;

SELECT RoadNetwork.id, RoadNetwork.g, st_distance(RoadNetwork.g, st_make_point(-118.32683220505714, 33.341658429469184)) AS distance
FROM RoadNetwork
ORDER BY distance ASC
LIMIT 1