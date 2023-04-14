from typing import Union

from fastapi import FastAPI

app = FastAPI()

sales = {
    1: { "item": "lat", "unit_price": 100, "quantity": 8 },
    2: { "item": "Drink", "unit_price": 200, "quantity": 8 },
    3: { "item": "fodd", "unit_price": 10, "quantity": 8 },
    4: { "item": "books", "unit_price": 4, "quantity": 8 },
    5: { "item": "papers", "unit_price": 100, "quantity": 8 }    
}

@app.get("/")
def read_root():
    return {"success": 'true', "message": "Hello Word", "data": "First Project Using FastAPIs" }

@app.get("/sales")
def sales():
    return {"success": 'true', "message": "All Sales", "data": sales }

@app.get("/sales/{sale_id}")
def read_item(sale_id: int):
    if sale_id in sales:
        return {"success": 'true', "message": "Sale", "data": sales[sale_id] }
    else:
        return {"success": 'false', "message": "Sale Not Found "}
