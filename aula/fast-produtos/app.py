from fastapi import FastAPI
from models.product import Product 

data =[
    Product(id=1, name= "Tenis Nike", description="Calçados", price=199),
    Product(id=2, name= "Camiseta", description="Roupas", price=59),
    Product(id=3, name= "Notebook", description="Eletrônicos", price=1999),
]

app = FastAPI()

@app.get("/")
def say_hello():
    return {"FastAPI": "Hello"}

@app.get("/{name}")
def say_hi(name:str):
    return {"Hello":name}

@app.get("/api/produtos")
def get_products():
    return data

@app.get("/api/produtos/{products_id}")
def get_products_by_id(products_id:int):
    """
    Endpoint que retorna um produto por Id
    """
    for product in data:
        if product.id == products_id:
            return product
    return {"404 - Not found"}