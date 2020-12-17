/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 * Author:  Pali
 * Created: Nov 12, 2020
 */

CREATE TABLE adminlogin (
	id serial PRIMARY KEY,
	txtusername VARCHAR ( 100 ) UNIQUE NOT NULL,
	txtpassword VARCHAR ( 20 ) NOT NULL 
);

CREATE TABLE category (
	categoryid serial PRIMARY KEY,
	txtcategoryname VARCHAR ( 500 ) UNIQUE NOT NULL,
	categoryimage oid,
	categorycreateby VARCHAR ( 500 ) UNIQUE NOT NULL,
	categorycreatedate TIMESTAMP NOT NULL 
);

CREATE TABLE country (
	countryid serial PRIMARY KEY,
	txtcountryname VARCHAR ( 500 ) UNIQUE NOT NULL,
	countrycreateby VARCHAR ( 500 ) UNIQUE NOT NULL,
	countrycreatedate TIMESTAMP NOT NULL 
);

CREATE TABLE state (
	stateid serial PRIMARY KEY,
        countryid INTEGER NOT NULL,
	txtstatename VARCHAR ( 500 ) UNIQUE NOT NULL,
	statecreateby VARCHAR ( 500 ) UNIQUE NOT NULL,
	statecreatedate TIMESTAMP NOT NULL,
        FOREIGN KEY (countryid)
        REFERENCES country (countryid)
);

CREATE TABLE city (
	cityid serial PRIMARY KEY,
        stateid INTEGER NOT NULL,
	txtcityname VARCHAR ( 500 ) UNIQUE NOT NULL,
	citycreateby VARCHAR ( 500 ) UNIQUE NOT NULL,
	citycreatedate TIMESTAMP NOT NULL,
        FOREIGN KEY (stateid)
        REFERENCES state (stateid)
);

CREATE TABLE heritagesite (
	siteid serial PRIMARY KEY,
	txtsitename VARCHAR ( 500 ) UNIQUE NOT NULL,
        txtalsoknow VARCHAR ( 500 ) UNIQUE NOT NULL,
        txtdescription text  NOT NULL,
        txtcoordinateslatitude VARCHAR ( 500 )  NOT NULL,
        txtcoordinateslongitude VARCHAR ( 500 )  NOT NULL,
        categoryid INTEGER NOT NULL,
        countryid INTEGER NOT NULL,
        stateid INTEGER NOT NULL,
        cityid INTEGER NOT NULL,
	sitecreateby VARCHAR ( 500 ) UNIQUE NOT NULL,
	sitecreatedate TIMESTAMP NOT NULL,
        FOREIGN KEY (categoryid)
        REFERENCES category (categoryid),
        FOREIGN KEY (countryid)
        REFERENCES country (countryid),
        FOREIGN KEY (stateid)
        REFERENCES state (stateid),
        FOREIGN KEY (cityid)
        REFERENCES city (cityid)
);

CREATE TABLE image (
	imageid serial PRIMARY KEY,
        image oid,
	txtimagename VARCHAR ( 500 ) UNIQUE NOT NULL,
        txtdescription text  NOT NULL,
        siteid INTEGER NOT NULL,
        isbanner BOOLEAN,
        isgeneralview BOOLEAN,
	imagecreateby VARCHAR ( 500 ) UNIQUE NOT NULL,
	imagecreatedate TIMESTAMP NOT NULL,
        FOREIGN KEY (siteid)
        REFERENCES heritagesite (siteid)
);


CREATE TABLE link (
	linkid serial PRIMARY KEY,
	txtlinkname VARCHAR ( 2000 ) UNIQUE NOT NULL,
        siteid INTEGER NOT NULL,
	linkcreateby VARCHAR ( 500 ) UNIQUE NOT NULL,
	linkcreatedate TIMESTAMP NOT NULL,
        FOREIGN KEY (siteid)
        REFERENCES heritagesite (siteid)
);



