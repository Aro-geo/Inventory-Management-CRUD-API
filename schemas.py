from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProductBase(BaseModel):
    ProductCode: str
    ProductName: str
    VendorID: Optional[int]
    WarehouseCode: Optional[str]
    CostPerItem: Optional[float]
    StockQuantity: Optional[int]
    TotalValue: Optional[float]
    ReorderLevel: Optional[int]
    DaysPerReorder: Optional[int]
    ItemReorderQuantity: Optional[int]
    SalesPrice: Optional[float]
    IsDiscontinued: Optional[bool]
    LastOrderDate: Optional[date]

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    CustomerName: str
    CustomerType: Optional[str]

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    CustomerID: int
    class Config:
        orm_mode = True

class SalesOrderBase(BaseModel):
    OrderNumber: str
    OrderDate: date
    CustomerID: int
    ProductCode: str
    WarehouseCode: str
    OrderQuantity: int
    UnitPrice: float
    Revenue: float
    Costs: float

class SalesOrderCreate(SalesOrderBase):
    pass

class SalesOrder(SalesOrderBase):
    class Config:
        orm_mode = True
