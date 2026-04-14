from fastapi import FastAPI
from models import Products
app = FastAPI()

@app.get('/') #first endpoint
def greet():
    return "Hello World"

products = [
    Products(id = 1, name ="phone", description = "budget phone", price = 99, quantity = 10),
    Products(id = 2, name = "laptop", description = "gaming laptop", price = 999, quantity = 6),
    Products(id = 5, name ="washing machine", description = "top laod", price = 99, quantity = 10),
    Products(id = 6, name = "tablet", description = "5 inch", price = 999, quantity = 6),
]

@app.get('/products')#second endpoint
def get_all_products():
    return products

@app.get('/product/{id}')
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    
    return "Product not found"

#add data
@app.post('/product')
def add_product(product: Products):
    products.append(product)
    return products

@app.put('/product')
def update_product(id:int, product:Products):#which particular id to update
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added successfully"
    return "No Products found"

@app.delete('/product')
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted Successfully"
    return "No product found"