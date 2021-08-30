USE TinyBenchmark;

SELECT Cities.name
FROM Cities
WHERE st_contains(Cities.boundary, st_make_point(-118.32683220505714, 33.341658429469184))