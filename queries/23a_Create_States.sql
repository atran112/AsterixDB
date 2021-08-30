CREATE TYPE StateType AS{
	ne_id : int,
	name: string,
	g : geometry
};

CREATE DATASET TempStates (StateType) PRIMARY KEY ne_id;
CREATE DATASET States (StateType) PRIMARY KEY ne_id;

LOAD DATASET TempStates using localfs
(('path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/bigDatasets/NE_states_provinces.json'),
('format'='adm'));

INSERT INTO States
(
	SELECT ne_id, name, g
	FROM TempStates
	WHERE name = "California"
);