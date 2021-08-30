SELECT *
FROM AllNodes, Buildings
WHERE st_intersects(AllNodes.g, Buildings.g)