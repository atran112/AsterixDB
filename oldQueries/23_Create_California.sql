USE TinyBenchmark;

CREATE TYPE StateType AS{
	ne_id : int,
	name: string,
	g : geometry
};

CREATE DATASET StatesTemp (StateType) PRIMARY KEY ne_id;
CREATE DATASET States (StateType) PRIMARY KEY ne_id;

LOAD DATASET States using localfs
(('path'='127.0.0.1:///Users/andretran/Documents/Projects/AsterixDB/bigDatasets/NE_states_provinces.json'),
('format'='adm'));

INSERT INTO States
(
	SELECT *
	FROM StatesTemp
	WHERE name = "California"
);
