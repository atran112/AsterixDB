DROP DATAVERSE BigBenchmark IF EXISTS;
CREATE DATAVERSE BigBenchmark;
USE BigBenchmark;

CREATE TYPE RoadNetworkType AS {
	id: UUID,
	g: geometry,
	attr0: string?,
	attr1: string?,
	attr2: string?,
	attr3: string?,
	attr4: string?
};

CREATE TYPE BuildingsType AS {
	id: UUID,
	g: geometry,
	attr0: string?,
	attr1: string?
};

CREATE TYPE AllNodesType AS {
	id: UUID,
	g: geometry,
	attr0: string?,
	attr1: string?
};

CREATE DATASET RoadNetwork (RoadNetworkType) PRIMARY KEY id AUTOGENERATED;
CREATE DATASET Buildings (BuildingsType) PRIMARY KEY id AUTOGENERATED;
CREATE DATASET AllNodes (AllNodesType) PRIMARY KEY id AUTOGENERATED;