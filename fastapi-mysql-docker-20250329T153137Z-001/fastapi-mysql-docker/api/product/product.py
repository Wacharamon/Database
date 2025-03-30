from fastapi import HTTPException,APIRouter
from database.query import query_get, query_create, query_update
from .models import ProductModel

def get_all_product():
    products = query_get("""
        SELECT  
            *
        FROM product
        """, ())
    return products

def get_product_by_id(id: int):
    product = query_get("""
        SELECT 
            *
        FROM product 
        WHERE id  = %s
        """, (id))
    return product

def add_product(product: ProductModel):
    last_row_id = query_create("""
                INSERT INTO product (
                    IceCreamName,
                    ToppingName,
                    Size,
                    Price       
                ) VALUES (%s, %s, %s, %s)
                """,
              (
                  product.IceCreamName,
                  product.ToppingName,
                  product.Size,
                  product.Price
              )
              )
    return last_row_id


def update_product(id: int,product: ProductModel):
    is_update = query_update("""
            UPDATE product 
                SET IceCreamName = %s,
                    ToppingName = %s,
                    Size = %s,
                    Price = %s       
                WHERE id = %s;
            """,
              (
                product.IceCreamName,
                product.ToppingName,
                product.Size,
                product.Price,
                id
              )
              )
    if is_update:
        product_update_data = product.dict()
        product_update_data.update({"id": id})
        return product_update_data
    else:
        return None
    
def delete_product(id: int):
    is_deleted = query_update("""
            DELETE FROM product 
                WHERE id = %s;
            """,
            (id)
    )
    return is_deleted