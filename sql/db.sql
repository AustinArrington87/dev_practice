# CREATE DB
CREATE DATABASE testDB;

# DROP DB 
DROP DATABASE testDB;

# BACKUP DB 

BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak';

# ONLY BACKUP CHANGES - DIFFERENTIAL
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak'
WITH DIFFERENTIAL;

# CREATE TABLE
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

# CREATE TABLE FROM EXISTING TABLE
SELECT customername, contactname
FROM customers;

# DROP TABLE TO DELETE

# ALTER TABLE
ALTER TABLE Customers
ADD Email varchar(255);

ALTER TABLE Persons
ADD DateOfBirth date;

ALTER TABLE Customers
DROP COLUMN Email;

ALTER TABLE table_name
ALTER COLUMN column_name datatype;

ALTER TABLE Persons
ALTER COLUMN DateOfBirth year;

ALTER TABLE Persons
DROP COLUMN DateOfBirth;

###############CONSTRAINTS
# NOT NULL - Ensures that a column cannot have a NULL value
# UNIQUE - Ensures that all values in a column are different
# PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
# FOREIGN KEY - Uniquely identifies a row/record in another table
# CHECK - Ensures that all values in a column satisfies a specific condition
# DEFAULT - Sets a default value for a column when no value is specified
# INDEX - Used to create and retrieve data from the database very quickly


CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int
);

ALTER TABLE Persons
MODIFY Age int NOT NULL;

# UNIQUE Constraints

# SQL Server / Oracle / MS access
CREATE TABLE Persons (
    ID int NOT NULL UNIQUE,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

#MYSQL
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (ID)
);

# Unique constraint - multiple columns
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person UNIQUE (ID,LastName)
);


# Unique constraint when table already created
ALTER TABLE Persons
ADD UNIQUE (ID);

# Primary Key -  uniquely identifies each . record in a table

#MYSQL
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);

# SQL / oracle / MS access
CREATE TABLE Persons (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

# PK constraint / multiple columns

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
);

# add PK w alter
ALTER TABLE Persons
ADD PRIMARY KEY (ID);

# add PK .-  multiple columns w alter
ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID,LastName);

# Drop PK - MySQL
ALTER TABLE Persons
DROP PRIMARY KEY;
# Drop PK - SQL Server / Oracle / MS access 
ALTER TABLE Persons
DROP CONSTRAINT PK_Person;

# FOREIGN KEY 
# used to link 2 tables together
# field or collection of fields in one table, refers to PK in another table

# Create FOREIGN KEY on PersonID column, when Orders Table Created 

# MYSQL
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);

#SQL Server / Oracle / MS access

CREATE TABLE Orders (
    OrderID int NOT NULL PRIMARY KEY,
    OrderNumber int NOT NULL,
    PersonID int FOREIGN KEY REFERENCES Persons(PersonID)
);


















