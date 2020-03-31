# selecting All - a 
SELECT * FROM Customers; 
# select columns 
SELECT CustomerName, City FROM Customers;
# select only distinct examples
SELECT DISTINCT Country FROM Customers;
# count distinct items 
SELECT COUNT(DISTINCT Country) FROM Customers;
####################################
# WHERE clause 
SELECT * FROM Customers WHERE Country='Mexico';
SELECT * FROM Customers WHERE Country='Germany' AND City='Berlin'; 
SELECT * FROM Customers WHERE City='Berlin' OR City='Munchen';

# NOT
SELECT * FROM Customers WHERE NOT Country='Germany';
# Combining Operators
SELECT * FROM Customers WHERE Country='Germany' AND (City='Berlin' OR City='Munchen');
SELECT * FROM Custsomers WHERE Country='Germany' AND NOT Country='USA';
######################################
# ORDER BY Keyword
SELECT * FROM Customers ORDER BY Country;
# ORDER By - descending
SELECT * FROM Customers ORDER BY Country DESC;
# ORDER By -  Several Clauses
# Orders by Country, if rows have same country, orders by CustomerName
SELECT * FROM Customers ORDER BY Country, CustomerName;
# if you want 2nd order in desc, do like this: 
SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;
########################
# INSERT INTO 
INSERT INTO Customers (CutomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'); 
# Specific Columns only
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
# IS NULL 
SELECT CustomerName, ContactName, Address
FROM Customers WHERE Address IS NULL;
# IS NOT
SELECT CustomerName, ContactName, Address
FROM Customers WHERE Address IS NOT NULL;
####### UPDATE TABLE
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City = "Frankfurt"
WHERE CustomerID = 1;
###Update Multiple Records 
UPDATE Customers
SET ContactName = 'Juan'
WHERE Country = 'Mexico';
# DELETE
DELETE FROM Customers WHERE CustomerName='Juan'
##########
# SELECT FROM TOP
SELECT TOP 3 * FROM Customers;
# Limit 3
SELECT * FROM Customers
LIMIT 3;
# Express s percentage 
SELECT TOP 50 PERCENT * FROM Customers;
###
SELECT TOP 3 * FROM Customers
WHERE Country='Germany'
LIMIT 3;
###### MIN & Max
# column name is 'Price'
SELECT MIN(Price) AS SmallestPrice
FROM Products;
##
SELECT MAX(Price) AS LargestPrice
FROM Products;
################
# Count, avg, sum
SELECT COUNT(ProductID)
FROM Products;
###
SELECT AVG(Price)
FROM Products;
## 
SELECT SUM(Quantity)
FROM OrderDetails; 
# all records where price equals certain amt
SELECT COUNT (*)
FROM Products
WHERE Price = 18;

####### LIKE #########
#Finds any values that start with "a"
SELECT * FROM Customers
WHERE CustomerName LIKE 'a%';
#Finds any values that end with "a"
SELECT * FROM Customers
WHERE CustomerName LIKE '%a';
# Finds any values that have "or" in any position
SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';
# Finds any values that have "r" in the second position
SELECT * FROM Customers
WHERE CustomerName LIKE '_r%';
# Finds any values that start with "a" and are at least 2 characters in length
SELECT * FROM Customers
WHERE CustomerName LIKE 'a_%';
# Finds any values that start with "a" and are at least 3 characters in length
SELECT * FROM Customers
WHERE CustomerName LIKE 'a__%';
# Finds any values that start with "a" and ends with "o"
SELECT * FROM Customers
WHERE ContactName LIKE 'a%o';
#  select where doesn't begin w a
SELECT * FROM Customers
WHERE ContactName NOT LIKE 'a%';

########## WILDCARD ############# 
# %	Represents zero or more characters	bl% finds bl, black, blue, and blob
# _	Represents a single character	h_t finds hot, hat, and hit
# []	Represents any single character within the brackets	h[oa]t finds hot and hat, but not hit
# ^	Represents any character not in the brackets	h[^oa]t finds hit, but not hot and hat
# -	Represents a range of characters	c[a-b]t finds cat and cbt

# Finds any values that starts with "a"
WHERE CustomerName LIKE 'a%'
# Finds any values that ends with "a"
WHERE CustomerName LIKE '%a'
# Finds any values that have "or" in any position
WHERE CustomerName LIKE '%or%'
# Finds any values that have "r" in the second position
WHERE CustomerName LIKE '_r%'	
# Finds any values that starts with "a" and are at least 3 characters in length
WHERE CustomerName LIKE 'a_%_%'
# Finds any values that starts with "a" and ends with "o"
WHERE ContactName LIKE 'a%o'

###
# begins w 'ber' 
SELECT * FROM Customers
WHERE City LIKE 'ber%';  
# ends with es
SELECT * FROM Customers
WHERE City LIKE '%es';
# first char can be anything
SELECT * FROM Customers
WHERE City LIKE '_ondon';
# 
SELECT * FROM Customers
WHERE City LIKE 'L_n_on';
# char list wildcard - city starting w b,s,p
SELECT * FROM Customers
WHERE City LIKE '[bsp]%';
# char list - city starting a - c
SELECT * FROM Customers
WHERE City LIKE '[a-c]%';
###############
### IN Operator ### --> replaces multiple OR clauses 
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');
######## 
### Between Operator
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
### BETWEEN With IN Operator
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1,2,3);
### Between Text
SELECT * FROM Products
WHERE ProductName BETWEEN "Carnarvon Tigers" AND "Chef Anton's Cajun Seasoning"
ORDER BY ProductName;
#### Between Date
SELECT * FROM Orders
WHERE OrderDate BETWEEEN '1996-07-01' AND '1996-07-31';
#### 
## Alias 
SELECT CustomerID AS Customer, ContactName AS [Contact Person]
FROM Customers;
# Multiple aliases
SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers; 
# MYSQL for multiple aliases
SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers;
# Aliase for table - multiple tables
SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName='Around the Horn' AND Customers.CustomerID=Orders.CustomerID;

########### JOIN ##################
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

# INNER JOIN: Returns records that have matching values in both tables
# LEFT OUTER JOIN: Returns all records from the left table, and the matched records from the right table
# LEFT OUTER JOIN: Returns all records from the left table, and the matched records from the right table
# FULL OUTER JOIN: Returns all records when there is a match in either left or right table

# TWO Inner Joins
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

# UNION - returns cities (distinct vals) from 2 different tabbles
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;

# UNION w WHERE
SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City;

# Do UNION ALL to include duplicAtes
# GROUP BY - USE TO COUNT
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;
# Order high to low 
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;

###GROUP BY

SELECT Shippers.ShipperName,COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName;

## HAVING -- select count of customers in different countries, over 5
# order high to low . 
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;

EXISTS
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price = 22);

#  ANY
SELECT ProductName
FROM Products
WHERE ProductID = ANY (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);

# ALL
SELECT ProductName 
FROM Products
WHERE ProductID = ALL (SELECT ProductID FROM OrderDetails WHERE Quantity = 10);

# SELECT INTO - creates NEW table
SELECT * INTO CustomersBackup2017
FROM Customers;
# copy into table in another DB 
SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'
FROM Customers;
# Copy only few columns
SELECT CustomerName, ContactName INTO CustomersBackup2017
FROM Customers;
# using WHERE statement 
SELECT * INTO CustomersGermany
FROM Customers
WHERE Country = 'Germany';
# SELECT from multiple tables 
SELECT Customers.CustomerName, Orders.OrderID
INTO CustomersOrderBackup2017
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
# Select into - empty table
SELECT * INTO CustomersOrderBackup2017
FROM Customers
WHERE 1 = 0;
# SELECT / INSERT INTO . 
INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers;
###  
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROM Suppliers;

### Case - Example  -- # creates new column QuantityText for result of filter
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;

# Orders by city, but when NULL, orders by Country 

SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);

# IF NULL 
# MYSQL  -- if unitsonOrder is null -- make it 0
SELECT ProductName, UnitPrice * (UnitsInStock + IFNULL(UnitsOnOrder, 0))
FROM Products;
# SQL Server - ISNULL
SELECT ProductName, UnitPrice * (UnitsInStock + ISNULL(UnitsOnOrder, 0))
FROM Products;

### STORED Procedure -- if you have SQL query you use over and over
CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;

# execute procedure" 
EXEC SelectAllCustomers;

### procedure with 1 parameter
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30)
AS
SELECT * FROM Customers WHERE City = @City
GO;
##
EXEC SelectAllCustomers @City = 'London';
######
# passing multiple parameters
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
GO;
## 
EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';

####














