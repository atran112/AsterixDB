SELECT *
FROM Buildings as B1, Buildings as B2
WHERE st_equals(B1.g, B2.g)