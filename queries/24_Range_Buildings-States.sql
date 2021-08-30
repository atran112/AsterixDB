SELECT st_area(Buildings.g) as Area
FROM Buildings, States
WHERE st_within(Buildings.g, States.g)