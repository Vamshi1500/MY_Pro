from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

list =  []

class User(BaseModel):
    name: str
    age: int
    email: str | None = None

    @field_validator("email")
    def mail(cls, mail):
        if "@" not in mail:
            raise ValueError("Invalid email format")
        return mail
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{id}")
def read_item(id:int): # id is a path parameter
    return {"item_id": id}

@app.get("/products/")
def get_product(name: str, price: float): # name and price are query parameters
    return {"name": name, "price": price}

@app.post("/user/")
def create_user(user: User):
    return 
    return {"message": "User {} created! with email {}".format(user.name, user.email)}

@app.put("/items/{id}")
def update_item(id: int, name: str):
    return {"message": "Item {} updated to {}".format(id, name)}

@app.delete("/items/{id}")
def delete_item(id: int):
    return {"message": "Item {} deleted".format(id)}