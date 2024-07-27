import sqlite3
from db import queries

db = sqlite3.connect("db/online_store.sqlite3")
cursor = db.cursor()


async def sql_create():
    if db:
        cursor.execute(queries.CREATE_TABLE_MARKET)
    db.commit()


async def sql_insert_market(name, size, price, productid, category, infoproduct, collection, photo):
    cursor.execute(queries.INSERT_PRODUCT, (name, size, price, productid, category, infoproduct, collection, photo))
    db.commit()


# async def sql_insert_detail_product(productid, category, infoproduct):
#     cursor.execute(queries.INSERT_PRODUCT, (
#         productid,
#         category,
#         infoproduct))
#     db.commit()


# async def sql_insert_product_collection(productid, collection):
#     cursor.execute(queries.INSERT_PRODUCT_COLLECTION, (
#         productid,
#         collection))
#     db.commit()
#
#
# async def sql_get_products():
#     cursor.execute(queries.GET_PRODUCTS)
#     products = cursor.fetchall()
#     return products
#
#
# async def sql_get_product_by_id(id):
#     cursor.execute(queries.GET_PRODUCT_BY_ID, (id,))
#     product = cursor.fetchone()
#     return product
#
#
# async def sql_get_number_of_products():
#     cursor.execute(queries.COUNT_PRODUCTS)
#     count = cursor.fetchone()[0]
#     return count
