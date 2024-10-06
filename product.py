import mysql.connector
import datetime


def createConn():
    global conn
    global cursor

    conn = mysql.connector.connect(
        host='localhost', password='sumanjeet83', user='root', database='shop')
    cursor = conn.cursor()


def add_product():
    while True:
        createConn()
        global conn
        global cursor

        name = input("Enter product name: ").lower().strip()
        quantity = int(input("Enter quantity of product: "))
        price = int(input("Enter price of one quantity: "))
        category = input("Enter category of product: ").lower().strip()
        discount = int(input("Enter discount per item: "))
        total = price * quantity

        print("\n--------DETAILS----------")
        print("Name:\t\t", name)      
        print("Quantity:\t", quantity)
        print("Price:\t\t", price)
        print("Category:\t", category)
        print("Total:\t\t", total)
        print("Discount:\t", discount)

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ans = input("\nDo you want to add details?(Y/n): ").lower().strip()
        if (ans == 'y'):
            query = ("insert into products(name, quantity, price, category, total, date, discount) values (%s, %s, %s, %s, %s, %s, %s)")
            values = (name, quantity, price, category, total, date, discount)
            cursor.execute(query, values)

            print("Details inserted successfully...")
            conn.commit()

            ques = input("\nDo you want to add more products?(Y/n): ").lower().strip()
            if (ques == 'n'):
                print("Exiting...")
                break


def show_all_products():
    createConn()
    global conn
    global cursor

    query = ("select * from products")

    cursor.execute(query)

    for (id, name, quantity, price, category, total, date, discount) in cursor:
        print("Id:\t\t {} \nName:\t\t {} \nQuantity:\t {} \nPrice:\t\t {} \nCategory:\t {} \nTotal:\t\t {} \nDate:\t\t {} \nDiscount:\t {}"
            .format(id, name, quantity, price, category, total, date, discount))
        print("-"*75)

    conn.commit()
    cursor.close()
    conn.close()


def show_product_by_id():
    while True:
        createConn()
        global conn
        global cursor

        query = ("select * from products where (id='%(id)s')")

        i = int(input("Enter id: "))

        values = {
            'id': i,
        }

        cursor.execute(query, values)

        for (id, name, quantity, price, category, total, date, discount) in cursor:
            print("\n--------DETAILS----------")
            print("Id:\t\t {} \nName:\t\t {} \nQuantity:\t {} \nPrice:\t\t {} \nCategory:\t {} \nTotal:\t\t {} \nDate:\t\t {} \nDiscount:\t {}"
                .format(id, name, quantity, price, category, total, date, discount))

        if cursor.rowcount > 0:
            pass

        else:
            print("\nNo product found!")

        ques = input("Do you want to see other product details? (y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break

        cursor.close()
        conn.close()


def update_product_full_info():
    while True:
        createConn()
        global conn
        global cursor

        id = int(input("Enter id of product you want to update: "))
        name = input("Enter new product name: ").lower().strip()
        quantity = int(input("Enter new quantity of product: "))
        price = int(input("Enter new price of product: "))
        category = input("Enter new category of product to update: ")
        discount = int(input("Enter new discount on product per item: "))
        total = price * quantity

        print("\n--------DETAILS----------")
        print("Name:\t\t", name)
        print("Quantity:\t", quantity)
        print("Price:\t\t", price)
        print("Category:\t", category)
        print("Total:\t\t", total)
        print("Discount\t", discount)

        ans = input("\nDo you want to update details?(Y/n): ").lower().strip()
        if (ans == 'y'):
            query = "update products set name = %s, quantity = %s, price = %s, category = %s, total = %s, discount = %s where id = %s"

            values = (name, quantity, price, category, total, discount, id)

            cursor.execute(query, values)
            conn.commit()
            print("Details updated successfully...")

            ques = input("\nDo you want to update more products?(Y/n): ").lower().strip()
            if (ques == 'n'):
                print("Exiting...")
                break

            cursor.close()
            conn.close()


def update_product_price():
    while True:
        createConn()
        global conn
        global cursor

        id = int(input("Enter id of product you want to update: "))
        price = int(input("Enter new price of product: "))

        query_for_quantity = ("select (quantity) from products where (id='%(id)s')")

        values_for_quantity = {
            'id': id,
        }

        cursor.execute(query_for_quantity, values_for_quantity)

        for quantity in cursor:
            product_quantity = quantity[0]

        total = price * product_quantity

        query = "update products set price = %s, total = %s where id = %s"

        values = (price, total, id)

        cursor.execute(query, values)
        conn.commit()
        print("Price updated successfully...")

        ques = input("\nDo you want to update more products Price?(Y/n): ").lower().strip()
        if (ques == 'n'):
            print("Exiting...")
            break

        cursor.close()
        conn.close()


def update_product_quantity():
    while True:
        createConn()
        global conn
        global cursor

        id = int(input("Enter id of product you want to update: "))
        quantity = int(input("Enter new quantity of product: "))

        query_for_price = ("select (price) from products where (id='%(id)s')")

        values_for_price = {
            'id': id,
        }

        cursor.execute(query_for_price, values_for_price)

        for price in cursor:
            product_price = price[0]

        total = quantity * product_price

        query = "update products set quantity = %s, total = %s where id = %s"

        values = (quantity, total, id)

        cursor.execute(query, values)
        conn.commit()
        print("Quantity updated successfully...")

        ques = input("\nDo you want to update more products quantity?(Y/n): ").lower().strip()
        if (ques == 'n'):
            print("Exiting...")
            break

        cursor.close()
        conn.close()


def search_product():
    while True:
        createConn()
        global conn
        global cursor

        name = input("Enter keyword to search product: ").lower().strip()

        query = "select * from products where name like %s or category like %s"
        values = (name + "%", name + "%")

        cursor.execute(query, values)

        for (id, name, quantity, price, category, total, date, discount) in cursor:
            print("\nId:\t\t {} \nName:\t\t {} \nQuantity:\t {} \nPrice:\t\t {} \nCategory:\t {} \nTotal:\t\t {} \nDate:\t\t {} \nDiscount:\t {}"
                .format(id, name, quantity, price, category, total, date, discount))
            
        if cursor.rowcount > 0:
            pass

        else:
            print("\nNo record found!")

        ques = input("Do you want to search more products? (y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break

        cursor.close()
        conn.close()

def delete_product():
    while True:
        createConn()
        global conn
        global cursor

        id = int(input("Enter id of product to delete: "))

        query = "delete from products where (id='%(id)s')"

        values = {
            'id' : id,
        }

        cursor.execute(query, values)
        conn.commit()
        print("Value deleted successfully...")

        ques = input("Do you want to delete more products? (Y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break


