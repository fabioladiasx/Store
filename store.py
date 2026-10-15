from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #1 -  line to make sure your webpage will be able to connect to the api
import sqlite3
from database import get_connection, create_tables
from schemas import ProductCreate,ProductUpdate,CategoryCreate,CategoryUpdate

create_tables()
app = FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_headers=["*"],allow_credentials=True,allow_methods=["*"])#2 -  line to make sure your webpage will be able to connect to the api

@app.get("/")
def greet():
    return {"message":"Welcome to our api !"}

# SQL



@app.post("/products")
def create_product(product:ProductCreate):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT id FROM categories
    WHERE id = ?
    """,(product.category_id,))

    category = cursor.fetchone()
    if category is None:
        return {"message":"category does not exist !"}
  


    cursor.execute("""
        INSERT INTO products
        (name,description,price,stock,category_id)

        VALUES (?,?,?,?,?)
    """ , (product.name,product.description,product.price,product.stock,product.category_id))

    connection.commit()
    connection.close()

    return {
        "message":"Product created !"
    }



# To get all the products in database
@app.get("/products")
def get_products():
    connection = get_connection()
    
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM products
    
    """)

    products = cursor.fetchall()

    connection.close()

    pds = []

    for product in products:
        pds.append(dict(product))

    return pds
    
# to get specific product from the database with id of the product
@app.get("/products/{product_id}")
def get_product(product_id:int):
    connection = get_connection()
        
    cursor = connection.cursor()


    cursor.execute("""
    SELECT * FROM products
    WHERE id = ?
    """,(product_id,))
# (10) --> int  , (10,) ---> tuple

    product = cursor.fetchone()
    connection.close()

    if product is None:
        return {"message":"product not found"}

    return dict(product)



# update or edit the product from the database
@app.put("/products/{product_id}")
def update_product(product_id:int,product:ProductCreate):
    connection = get_connection()
            
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM products
        WHERE id = ?
        """,(product_id,))

    existing_product = cursor.fetchone()

    if existing_product is None:
        connection.close()

        return {"message":"Product not found"}

    cursor.execute("""
    UPDATE products

    SET
        name = ?,
        description = ?,
        price=?,
        stock=?,
        category_id=?

    WHERE id = ?
    
    """,(product.name,product.description,product.price,product.stock,product.category_id,product_id))

    connection.commit()

    connection.close()

    return {"message":"Product Updated !"}


# delete a specific product from database
@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    connection = get_connection()
                
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM products
        WHERE id = ?
        """,(product_id,))
    
    existing_product = cursor.fetchone()

    if existing_product is None:
        connection.close()

        return {"message":"Product not found"}

    cursor.execute("""
    DELETE FROM products
    WHERE id = ?
    """,(product_id,))


    connection.commit()
    connection.close()

    return {"message":"Product deleted !"}


# to create a new category in database
@app.post("/categories")
def create_category(category:CategoryCreate):
    connection = get_connection()
                    
    cursor = connection.cursor()
    cursor.execute("""
            INSERT INTO categories
            (name)
    
            VALUES (?)
        """ , (category.name,))
    connection.commit()
    connection.close()

    return {"message":"Category created"}


# to get all the categories from the database
@app.get("/categories")
def get_categories():
    connection = get_connection()
    
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM categories
    
    """)

    categories = cursor.fetchall()

    connection.close()

    cts = []

    for category in categories:
        cts.append(dict(category))

    return cts

# get specific category
@app.get("/categories/{category_id}")
def get_categroy(category_id:int):
    connection = get_connection()
        
    cursor = connection.cursor()


    cursor.execute("""
    SELECT * FROM categories
    WHERE id = ?
    """,(category_id,))
# (10) --> int  , (10,) ---> tuple

    category = cursor.fetchone()
    connection.close()

    if category is None:
        return {"message":"category not found"}

    return dict(category)

# update or edit the product from the database
@app.put("/categories/{categories_id}")
def update_category(category_id:int,category:CategoryUpdate):
    connection = get_connection()
            
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM categories
        WHERE id = ?
        """,(category_id,))

    existing_category = cursor.fetchone()

    if existing_category is None:
        connection.close()

        return {"message":"category not found"}

    cursor.execute("""
    UPDATE category

    SET
        name = ?,
  
    WHERE id = ?
    
    """,(category.name,category_id))

    connection.commit()

    connection.close()

    return {"message":"Product Updated !"}



@app.delete("/categories/{category_id}")
def delete_category(category_id:int):
    connection = get_connection()
                
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM categories
        WHERE id = ?
        """,(category_id,))
    
    existing_category = cursor.fetchone()

    if existing_category is None:
        connection.close()

        return {"message":"Category not found"}

    cursor.execute("""
    DELETE FROM categories
    WHERE id = ?
    """,(category_id,))


    connection.commit()
    connection.close()

    return {"message":"Category deleted !"}