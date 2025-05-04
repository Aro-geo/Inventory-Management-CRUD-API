CREATE DATABASE inventory_management;
USE inventory_management;
-- Create table for Vendors
CREATE TABLE Vendors (
    VendorID INT AUTO_INCREMENT PRIMARY KEY,
    VendorName VARCHAR(100) UNIQUE NOT NULL
);

-- Create table for Warehouses
CREATE TABLE Warehouses (
    WarehouseCode VARCHAR(10) PRIMARY KEY,
    LocationName VARCHAR(100)
);

-- Create table for Products
CREATE TABLE Products (
    ProductCode VARCHAR(20) PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    VendorID INT,
    WarehouseCode VARCHAR(10),
    CostPerItem DECIMAL(10,2),
    StockQuantity INT,
    TotalValue DECIMAL(10,2),
    ReorderLevel INT,
    DaysPerReorder INT,
    ItemReorderQuantity INT,
    SalesPrice DECIMAL(10,2),
    IsDiscontinued BOOLEAN,
    LastOrderDate DATE,
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID),
    FOREIGN KEY (WarehouseCode) REFERENCES Warehouses(WarehouseCode)
);

-- Create table for Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(100) UNIQUE NOT NULL,
    CustomerType VARCHAR(50)
);

-- Create table for Sales Orders
CREATE TABLE SalesOrders (
    OrderNumber VARCHAR(20) PRIMARY KEY,
    OrderDate DATE NOT NULL,
    CustomerID INT,
    ProductCode VARCHAR(20),
    WarehouseCode VARCHAR(10),
    OrderQuantity INT,
    UnitPrice DECIMAL(10,2),
    Revenue DECIMAL(10,2),
    Costs DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductCode) REFERENCES Products(ProductCode),
    FOREIGN KEY (WarehouseCode) REFERENCES Warehouses(WarehouseCode)
);
