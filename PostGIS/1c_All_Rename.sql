ALTER TABLE Buildings
RENAME COLUMN wkb_geometry to g;

ALTER TABLE RoadNetwork
RENAME COLUMN wkb_geometry to g;

ALTER TABLE AllNodes
RENAME COLUMN wkb_geometry to g;