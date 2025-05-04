from sqlalchemy import Column, Integer, String, Date, ForeignKey, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Vendor(Base):
    __tablename__ = "Vendors"
    VendorID = Column(Integer, primary_key=True, index=True)
    VendorName = Column(String(100), unique=True, nullable=False)

class Warehouse(Base):
    __tablename__ = "Warehouses"
    WarehouseCode = Column(String(10), primary_key=True)
    LocationName = Column(String(100))

class Product(Base):
    __tablename__ = "Products"
    ProductCode = Column(String(20), primary_key=True, index=True)
    ProductName = Column(String(100), nullable=False)
    VendorID = Column(Integer, ForeignKey("Vendors.VendorID"))
    WarehouseCode = Column(String(10), ForeignKey("Warehouses.WarehouseCode"))
    CostPerItem = Column(DECIMAL(10,2))
    StockQuantity = Column(Integer)
    TotalValue = Column(DECIMAL(10,2))
    ReorderLevel = Column(Integer)
    DaysPerReorder = Column(Integer)
    ItemReorderQuantity = Column(Integer)
    SalesPrice = Column(DECIMAL(10,2))
    IsDiscontinued = Column(Boolean)
    LastOrderDate = Column(Date)

class Customer(Base):
    __tablename__ = "Customers"
    CustomerID = Column(Integer, primary_key=True, index=True)
    CustomerName = Column(String(100), unique=True, nullable=False)
    CustomerType = Column(String(50))

class SalesOrder(Base):
    __tablename__ = "SalesOrders"
    OrderNumber = Column(String(20), primary_key=True, index=True)
    OrderDate = Column(Date, nullable=False)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"))
    ProductCode = Column(String(20), ForeignKey("Products.ProductCode"))
    WarehouseCode = Column(String(10), ForeignKey("Warehouses.WarehouseCode"))
    OrderQuantity = Column(Integer)
    UnitPrice = Column(DECIMAL(10,2))
    Revenue = Column(DECIMAL(10,2))
    Costs = Column(DECIMAL(10,2))
