USE TinyBenchmark;

SELECT st_length(RoadNetwork.g) as Length
FROM RoadNetwork, States
WHERE st_within(RoadNetwork.g, States.boundary);