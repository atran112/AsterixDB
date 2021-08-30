USE BigBenchmark;

SELECT UrbanAreas.name
FROM UrbanAreas
WHERE st_contains(UrbanAreas.g, st_make_point(-118.32683220505714, 33.341658429469184))