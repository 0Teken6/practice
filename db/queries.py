CREATE_TABLE_MARKET = """
    CREATE TABLE IF NOT EXISTS online_market
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255), 
    productid VARCHAR(255),
    category VARCHAR(255),
    infoproduct VARCHAR(255),
    collection VARCHAR(255),
    photo TEXT
    )
"""

INSERT_PRODUCT = """
    INSERT INTO online_market(name, size, price, productid, category, infoproduct, collection, photo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

# CREATE_TABLE_PRODUCT_DETAILS = """
#     CREATE TABLE IF NOT EXISTS products_detail
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     productid VARCHAR(255),
#     category VARCHAR(255),
#     infoproduct VARCHAR(255)
#     )
# """
#
# CREATE_TABLE_PRODUCT_COLLECTION = """
#     CREATE TABLE IF NOT EXISTS collection_products
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     productid VARCHAR(255),
#     collection VARCHAR(255)
#     )
# """
#
# INSERT_PRODUCT_COLLECTION = """
#     INSERT INTO collection_products(productid, collection)
#     VALUES (?, ?)
# """
#
# INSERT_DETAIL_PRODUCT = """
#     INSERT INTO products_detail(productid, category, infoproduct)
#     VALUES (?, ?, ?)
# """
#
# GET_PRODUCTS = """
#     SELECT os.name, os.size, os.price, os.productid, os.photo, pd.category, pd.infoproduct, cp.collection FROM online_store os
#     INNER JOIN products_detail pd ON os.productid = pd.productid
#     INNER JOIN collection_products cp ON os.productid = cp.productid
# """
#
# GET_PRODUCT_BY_ID = """
#     SELECT os.name, os.size, os.price, os.productid, os.photo, pd.category, pd.infoproduct, cp.collection FROM online_store os
#     INNER JOIN products_detail pd ON os.productid = pd.productid
#     INNER JOIN collection_products cp ON os.productid = cp.productid
#     WHERE os.id = ?
# """
#
# COUNT_PRODUCTS = """
#     SELECT COUNT(*) FROM online_store
# """
