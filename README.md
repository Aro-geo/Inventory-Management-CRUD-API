# Inventory Management CRUD API with MySQL & FastAPI

## 📌 Project Description

This project is a full-featured Inventory Management System that includes:

- A relational database schema built in MySQL
- An interactive RESTful CRUD API using FastAPI
- Full support for managing **Products**, **Customers**, and **Sales Orders**

The system is designed to handle basic inventory operations such as product registration, customer management, order tracking, and pricing.

---

## ⚙️ Technologies Used

- **MySQL** – for database design and data persistence
- **FastAPI** – for building the REST API
- **SQLAlchemy** – ORM for database interaction
- **Pydantic** – for data validation and serialization
- **Uvicorn** – ASGI server to run FastAPI app

---

## 🏗️ Database Schema Overview

The project contains five main tables:
- `Products`
- `Vendors`
- `Warehouses`
- `Customers`
- `SalesOrders`

ER Diagram: ![Inventory ERD](https://github.com/user-attachments/assets/45ff0467-e70b-4321-8735-01a1597dfc5f)


---

## 🚀 How to Run the Project

### ✅ Prerequisites

- Python 3.8+
- MySQL Server
- Git

### 📦 Install Dependencies

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/inventory-api.git
   cd inventory-api
