SELECT *
FROM AllNodes
WHERE st_intersects(AllNodes.g, st_geom_from_text('POLYGON((-118.62762451171875 33.224903086263964, -117.12799072265625 33.224903086263964, -117.12799072265625 34.168635904722734, -118.62762451171875 34.168635904722734, -118.62762451171875 33.224903086263964))'))