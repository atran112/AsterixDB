USE BigBenchmark;

SELECT st_length(RoadNetwork.g) as Length
FROM RoadNetwork, States
WHERE st_within(RoadNetwork.g, States.g);