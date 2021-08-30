SELECT States.name, SUM(st_length(RoadNetwork.g)) as TotalLength
FROM States, RoadNetwork
WHERE st_contains(States.g, RoadNetwork.g)
GROUP BY States.name