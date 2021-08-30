SELECT *
FROM RoadNetwork, Buildings
WHERE st_touches(RoadNetwork.g, Buildings.g)