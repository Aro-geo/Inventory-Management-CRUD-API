from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{product_code}", response_model=schemas.Product)
def get_product(product_code: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.ProductCode == product_code).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_code}", response_model=schemas.Product)
def update_product(product_code: str, product_data: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.ProductCode == product_code).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product_data.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{product_code}")
def delete_product(product_code: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.ProductCode == product_code).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}
