SELECT *
FROM Buildings, RoadNetwork
WHERE st_intersects(Buildings.g, RoadNetwork.g)