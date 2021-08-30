SELECT States.name, COUNT(*) as TotalBuildings
FROM States, Buildings
WHERE st_contains(States.g, Buildings.g)
GROUP BY States.name