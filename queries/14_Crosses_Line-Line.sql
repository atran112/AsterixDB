SELECT *
FROM RoadNetwork as RN1, RoadNetwork as RN2
WHERE st_crosses(RN1.g, RN2.g)