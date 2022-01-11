from logging import exception
import pymysql
import os
from dotenv import load_dotenv
import csv

# def test_connections():
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection

def execute_query(*sql):
    
    try:
        connection = pymysql.connect(host, user, password, database, autocommit=True)
        cursor = connection.cursor()
        
        # Execute
        cursor.execute(*sql)
        rows = cursor.fetchall()
        
        # Close down
        cursor.close()

    finally:
        connection.close()
    
    return rows

def get_data(sql):
    data = execute_query(sql)
    return data

def print_products():
    products = get_data("select * from products")
    for row in products:
        print(f'ID {row[0]}: {row[1]}: £{row[2]}')

def add_product(name: str, price: str):
    sql = f"insert into products (product_name, price) values ('{name}','{price}')"
    execute_query(sql)

def edit_product(id: int, product: str, price: float):     
    if product == "":
        pass
    else:
        execute_query("UPDATE products SET product_name = %s WHERE product_id = %s", (product, id))

    if price is not type(float):
        execute_query("UPDATE products SET price = %s WHERE product_id = %s", (price, id))
    else:
        pass
  
def delete_product(id: int):
    sql = ("DELETE FROM products WHERE product_id = %s" % (id))
    execute_query(sql)


def print_couriers():
    couriers = get_data("select * from couriers")
    for row in couriers:
        print(f'ID {row[0]}: {row[1]}: {row[2]}: {row[3]}')

def add_courier(first_name: str, last_name: str, phone_number: str):
    sql = f"insert into couriers (first_name, last_name, phone_number ) values ('{first_name}','{last_name}','{phone_number}')"
    execute_query(sql)

def edit_courier(id: int, first_name: str, last_name:str, phone_number: str):     
    if first_name == "":
        pass
    else:
        execute_query("UPDATE couriers SET first_name = %s WHERE courier_id = %s", (first_name, id))

    if last_name == "":
        pass
    else:
        execute_query("UPDATE couriers SET last_name = %s WHERE courier_id = %s", (last_name, id))

    if phone_number == "":
        pass
    else:
        execute_query("UPDATE couriers SET phone_number = %s WHERE courier_id = %s", (phone_number, id))
    
def delete_courier(id: int):
    sql = ("DELETE FROM couriers WHERE courier_id = %s" % (id))
    execute_query(sql)


def print_customers():
    customers = get_data("select * from customers")
    for row in customers:
        print(f"ID: {row[0]}: {row[1]}: {row[2]}: {row[3]}: {row[4]}: {row[5]} ")

def add_customer(first_name: str, last_name: str, phone_number: str, street_town: str, postcode: str):
    sql = f"insert into customers (first_name, last_name, phone_number, street_town, postcode ) values ('{first_name}','{last_name}','{phone_number}','{street_town}','{postcode}')"
    execute_query(sql)

def edit_customer(id: int, first_name: str, last_name: str, phone_number: str, street_town: str, postcode: str):
    if first_name:
        execute_query("UPDATE customers SET first_name = %s WHERE customer_id = %s", (first_name, id))
    else:
        pass
    if last_name:
        execute_query("UPDATE customers SET last_name = %s WHERE customer_id = %s", (last_name, id))
    else:
        pass
    if phone_number:
        execute_query("UPDATE customers SET phone_number = %s WHERE customer_id = %s", (phone_number, id))
    else:
        pass
    if street_town:
        execute_query("UPDATE customers SET street_town = %s WHERE customer_id = %s", (street_town, id))
    else:
        pass
    if postcode:
        execute_query("UPDATE customers SET postcode = %s WHERE customer_id = %s", (postcode, id))
    else:
        pass
    
def delete_customer(id: int):
    try:
        sql = ("DELETE FROM customers WHERE customer_id = %s" % (id))
        execute_query(sql)
    except exception:
        print("An error ocurred")

def print_orders():
    orders = get_data("SELECT * from orders")
    for row in orders:
        print(f'Order ID: {row[0]} Customer ID: {row[1]} Courier ID: {row[2]} Product ID: {row[3]} Status: {row[4]}')

def add_orders(customer_id: int, courier_id: int, product_id: int):
    order_status = "Processing"
    for row in product_id:
        sql = f"insert into orders (customer_id, courier_id, product_id, order_status) values ('{customer_id}','{courier_id}','{row}','{order_status}')"
        execute_query(sql)

def edit_orders(order_id: int, customer_id: int, courier_id:int, product_id:int):
    order_status = "Processing"     
    if customer_id:
        execute_query("UPDATE orders SET customer_id = %s, order_status = %s WHERE order_id = %s", (customer_id, order_status, order_id))
    else:
        pass

    if courier_id:
        execute_query("UPDATE orders SET courier_id = %s, order_status = %s WHERE order_id = %s", (courier_id, order_status, order_id))
    else:
        pass

    if product_id:
        execute_query("UPDATE orders SET product_id = %s, order_status = %s WHERE order_id = %s", (product_id, order_status, order_id))
    else:
        pass
    
def delete_order(id: int):
    sql = ("DELETE FROM orders WHERE order_id = %s" % (id))
    execute_query(sql)






def print_list(list_name):
    print("\n")
    for rows in list_name:
         print(list_name)

def write_csv_file(file_name, list_name):
    fieldnames = list_name[0].keys()
    with open(file_name, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(list_name)


def execute_dict_query(*sql):
    
    try:
        connection = pymysql.connect(host, user, password, database, autocommit=True)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        
        # Execute
        cursor.execute(*sql)
        rows = cursor.fetchall()
        
        # Close down
        cursor.close()

    finally:
        connection.close()
    
    return rows

def get_dict_data(sql):
    data = execute_dict_query(sql)
    return data



