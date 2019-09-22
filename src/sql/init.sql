CREATE EXTENSION postgis;

CREATE TABLE accounts (
	customerid varchar NOT NULL,
	"type" varchar NULL,
	opendate date NULL,
	accountid varchar NULL,
	balance numeric NULL
);

CREATE TABLE customers (
	cid varchar NOT NULL,
	givenname varchar NOT NULL,
	surname varchar NOT NULL,
	age int4 NULL,
	gender varchar NULL,
	latitude numeric NULL,
	longitude numeric NULL,
	totalincome numeric NULL,
	relationshipstatus varchar NULL,
	habitationstatus varchar NULL,
	geog elevate.geography NULL
);
