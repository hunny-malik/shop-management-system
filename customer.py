import mysql.connector
import datetime


def createConn():
    global conn
    global cursor

    conn = mysql.connector.connect(
        host='localhost', password='sumanjeet83', user='root', database='shop')
    cursor = conn.cursor()

def add_customer():
    while True:
        createConn()
        global cursor
        global conn

        name = input("Enter customer Name: ").lower().strip()
        address = input("Enter customer Address: ")
        phone = input("Enter customer Phone number: ")
        email = input("Enter customer Email: ")

        print("\n--------DETAILS----------")
        print("Name:\t\t", name)
        print("Address:\t", address)
        print("Phone:\t\t", phone)
        print("Email:\t\t", email)

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ans = input("\nDo you want to add details?(Y/n): ").lower().strip()
        if (ans == 'y'):
            query = ("insert into customers(name, address, phone, email, date) values ( %s, %s, %s, %s, %s)")
            values = (name, address, phone, email, date)
            cursor.execute(query, values)

            print("Details inserted successfully...")
            conn.commit()

            ques = input("\nDo you want to add more customers?(Y/n): ").lower().strip()
            if (ques == 'n'):
                print("Exiting...")
                break


def show_all_customers():
    createConn()
    global conn
    global cursor

    query = ("select * from customers")

    cursor.execute(query)

    for (id, name, address, phone, email, date) in cursor:
        print("Id:\t\t {} \nName:\t\t {} \nAddress:\t {} \nPhone:\t\t {} \nEmail:\t\t {} \nDate:\t\t {}"
            .format(id, name, address, phone, email, date))
        print("-"*75)

    conn.commit()
    cursor.close()
    conn.close()


def show_customer_by_id():
    while True:
        createConn()
        global conn
        global cursor

        query = ("select * from customers where (id='%(id)s')")

        i = int(input("Enter id: "))

        values = {
            'id': i,
        }

        cursor.execute(query, values)

        for (id, name, address, phone, email, date) in cursor:
            print("\n--------DETAILS----------")
            print("Id:\t\t {} \nName:\t\t {} \nAddress:\t {} \nPhone:\t\t {} \nEmail:\t\t {} \nDate:\t\t {}"
            .format(id, name, address, phone, email, date))

        if cursor.rowcount > 0:
            pass

        else:
            print("\nNo customer found!")

        ques = input("Do you want to see other customer details? (y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break

        cursor.close()
        conn.close()


def update_customer_full_info():
    while True:
        createConn()
        global conn
        global cursor

        id = int(input("Enter id of customer you want to update: "))
        address = input("Enter new address of customer: ")
        phone = input("Enter new phone number of customer: ")
        email = input("Enter new email of customer: ")

        query_to_view_name = ("select (name) from customers where (id='%(id)s')")

        value_for_name = {
            'id' : id,
        }

        cursor.execute(query_to_view_name, value_for_name)

        for (name) in cursor:
            name = name[0]

        print("\n--------DETAILS----------")
        print("Name:\t\t", name)
        print("Address:\t", address)
        print("Phone:\t\t", phone)
        print("Email:\t\t", email)

        ans = input("\nDo you want to update details?(Y/n): ").lower().strip()
        if (ans == 'y'):
            query = "update customers set address = %s, phone = %s, email = %s where id = %s"

            values = (address, phone, email, id)

            cursor.execute(query, values)
            conn.commit()
            print("Details updated successfully...")

            ques = input("\nDo you want to update more customers?(Y/n): ").lower().strip()
            if (ques == 'n'):
                print("Exiting...")
                break

            cursor.close()
            conn.close()


def search_customer():
    while True:
        createConn()
        global conn
        global cursor

        name = input("Enter keyword to search customer: ").lower().strip()

        query = "select * from customers where name like %(name)s"
        values = {
            'name': name + "%",
        }

        cursor.execute(query, values)

        for (id, name, address, phone, email, date) in cursor:
            print("\nId:\t\t {} \nName:\t\t {} \nAddress:\t {} \nPhone:\t\t {} \nEmail:\t\t {} \nDate:\t\t {}"
            .format(id, name, address, phone, email, date))
            
        if cursor.rowcount > 0:
            pass

        else:
            print("\nNo record found!")

        ques = input("Do you want to search more customers? (y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break

        cursor.close()
        conn.close()


def delete_customers():
    while True:
        createConn()
        global conn
        global cursor

        id = int(input("Enter id of customer to delete: "))

        query = "delete from customers where (id='%(id)s')"

        values = {
            'id' : id,
        }

        cursor.execute(query, values)
        conn.commit()
        print("Customer deleted successfully...")

        ques = input("Do you want to delete more customers? (Y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break

