from pydantic import BaseModel



class ProductCreate(BaseModel):
    name:str
    description:str
    price:float
    stock:int
    category_id:int


class ProductUpdate(BaseModel):
    name:str
    description:str
    price:float
    stock:int
    category_id:int

class CategoryCreate(BaseModel):
    name : str

class CategoryUpdate(BaseModel):
    name : str