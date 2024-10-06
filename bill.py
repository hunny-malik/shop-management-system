import mysql.connector
import datetime
import os
import time
import sys
#import website
#import threading

global final_amount
final_amount = 0

def createConn():
    global conn
    global cursor

    conn = mysql.connector.connect(
        host='localhost', password='sumanjeet83', user='root', database='shop')
    cursor = conn.cursor()


def update_status(status):
    with open("payment_status.txt", "w") as status_file:
        status_file.write(status)


def read_last_line(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()
    return None


'''def animation():

    animation = "|/-\\"
    for _ in range(100):
        for char in animation:
            sys.stdout.write(f"\rPayment Status: {char}")
            sys.stdout.flush()
            time.sleep(0.1)

    status = read_last_line("payment_status.txt")

    sys.stdout.write("\rPayment Status: {}\n".format(status))
    time.sleep(2) '''


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def write_final_amount_to_file(final_amount):
    file_path = os.path.join(os.path.dirname(__file__), "amount.txt")
    with open(file_path, "w") as file:
        file.write(str(final_amount))


def update_amount(amount):
    with open("amount.txt", "w") as status_file:
        status_file.write(amount)

def cart():
    createConn()
    global conn
    global cursor

    global name
    name = input("Enter customer name: ")

    global phone
    phone = input("Enter customer phone number: ")

    global date 
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    query_for_product = "select name, quantity, price, category, discount from products"
    cursor.execute(query_for_product)

    product_data = [(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
    product_name = [row[0] for row in product_data]
    product_quantity = [row[1] for row in product_data]
    product_price = [row[2] for row in product_data]
    product_category = [row[3] for row in product_data]
    product_discount = [row[4] for row in product_data]

    global user_cart
    user_cart =[]

    global cart_quantity
    cart_quantity = []

    global cart_price
    cart_price = []

    global cart_category
    cart_category = []

    global cart_total
    cart_total = []

    global cart_discount
    cart_discount = []

    while True:

        createConn()
        user_product_name = input("Enter the name of product: ").lower().strip()
        if user_product_name in product_name:
            idx = product_name.index(user_product_name)
            user_product_quantity = int(input("\nEnter Quantity: "))
            if user_product_quantity <= product_quantity[idx]:
                user_cart.append(user_product_name)
                cart_quantity.append(user_product_quantity)
                cart_price.append(product_price[idx])
                total = user_product_quantity * product_price[idx]
                cart_total.append(total)
                user_product_discount = product_discount[idx] * user_product_quantity
                cart_discount.append(user_product_discount)
                user_product_category = product_category[idx]
                cart_category.append(user_product_category)

            else:
                print("Quantity not available...")

        else:
            print("Product not available...")

        ques = input("Do u want to add more products?(Y/n)").lower().strip()
        if ques == 'n':
            print("S.no \tName \t\tQuantity \tDiscount")
            sno = 1
            for i in range(len(user_cart)):
                print(str(sno) + "\t" + str(user_cart[i]) + "\t\t" + str(cart_quantity[i]) + "\t\t" + str(cart_discount[i]))
                sno += 1

            while True:
                ques = input("Do you want to remove any product?(y/n): ").lower().strip()
                if ques == 'n':
                    for i in range(len(user_cart)):
                        idx = product_name.index(user_cart[i])
                        update_quantity = product_quantity[idx] - cart_quantity[i]
                        update_total = update_quantity * product_price[idx]

                        query = "update products set quantity = %s, total = %s where name = %s"
                        values = (update_quantity, update_total, user_cart[i])

                        cursor.execute(query, values)
                    break

                else:
                    delete_name = input("Enter name of product you want to remove: ").lower().strip()
                    idx = user_cart.index(delete_name)
                    print(idx)
                    user_cart.pop(idx)
                    cart_category.pop(idx)
                    cart_discount.pop(idx)
                    cart_price.pop(idx)
                    cart_quantity.pop(idx)
                    cart_total.pop(idx)



            conn.commit()
            break


def create_bill():
    cart()
    global user_cart, cart_price, cart_quantity, cart_total,cart_category, cart_discount, name, date, phone, final_amount

    payment_method = input("How would you like to pay? ")

    time.sleep(2)
    clear_terminal()

    print("\n\n" + "-"*38 + "INVOICE" + "-"*38)
    print("Date:\t\t\t\t\t\t\t\t" + date)
    print("\nBill to: ")
    print("Name: " + name)
    print("Phone: " + phone)


    print("\n{:<20} {:<15} {:<10} {:<10} {:<15} {:<10}".format(
        "Product", "Category", "Quantity", "Price", "Total", "Discount"
    ))
    print("-" * 83)

    sub_total = sub_discount = grand_total = final_amount = 0
    gst = 18

    if not user_cart:
        print("No Product Added!")

    else:
        if len(user_cart) == len(cart_category) == len(cart_quantity) == len(cart_price) == len(cart_total) == len(cart_discount):
            for i in range(len(user_cart)):
                print("{:<20} {:<15} {:<10} {:<10} {:<15} {:<10}".format(
                    user_cart[i],
                    cart_category[i],
                    cart_quantity[i],
                    cart_price[i],
                    cart_total[i],
                    cart_discount[i]
                ))

                sub_total += cart_total[i]
                sub_discount += cart_discount[i]
                grand_total = sub_total - sub_discount

                gst = 18

                final_amount = grand_total + (grand_total * (18/100))
        else:
            print("Error: Lists have different lengths.")


    print("-" * 83)
    print("SUB TOTAL:\t\t\t\t\t\t   " + str(sub_total) + "\t           " + str(sub_discount))
    print("GRAND TOTAL(after applying discount):\t\t\t\t\t   " + str(grand_total))
    print("GST: \t\t\t\t\t\t\t\t\t   " + str(gst) + "%")
    print("-" * 83)
    print("FINAL AMOUNT(including all GST & taxes)\t\t\t\t\t   ₹" + str(final_amount))
    print("\nPayment Method: " + payment_method)
    write_final_amount_to_file(final_amount)

    '''if not user_cart:
        print("Payment Status: No product added!")

    else:
        animation_thread = threading.Thread(target=animation)
        animation_thread.start()

        animation_thread.join()'''

    n = 0
    while True:
        animation = "|/-\\"
        for _ in range(5):
            for char in animation:
                sys.stdout.write(f"\rPayment Status: {char}")
                sys.stdout.flush()
                time.sleep(0.1)

        status = read_last_line("payment_status.txt")
        if status == 'PAID':
            sys.stdout.write("\rPayment Status: {}\n".format(status))
            break

        time.sleep(0.1)
        n += 0.1

        if n == 30:
            sys.stdout.write("\rPayment Status: {}\n".format(status))
            break

    time.sleep(2)

    update_status("Failed")
    print("-" * 83)
    print("Thank you for shopping here...")
    print("All terms & conditions applied...")
    print("-" * 83)
    print("Contact Details: ")
    print("HUNNY MALIK")
    print("+91 8264886998")
    print("hunny.malik200524@gmail.com")
    print("-" * 83)
    print(" " * 36 + "VISIT AGAIN" + " " * 36)
    update_amount("0")

    if final_amount == 0:
        pass

    else:
        query_for_sales = "insert into sales(name, phone, total_without_gst, total_with_gst, date) values(%s, %s, %s, %s, %s)"
        values_for_sales = (name, phone, grand_total, final_amount, date)

        cursor.execute(query_for_sales, values_for_sales)
    conn.commit()

    createConn()

    ques = input("\n\nWould you like to rate our store?(Y/n)").lower().strip()
    if ques == 'y':
        createConn()
        star_rating = int(input("Star? (0-5): "))
        message = input("Please give your review: ")

        print("Thank you for sharing your review...")

        query = "insert into reviews(name, star, message, date) values (%s, %s, %s, %s)"
        values = (name, star_rating, message, date)

        cursor.execute(query, values)

        conn.commit()
        conn.close()
        cursor.close()


    else:
        star_rating = None
        message = None


def see_products():
    createConn()
    global conn
    global cursor

    query_for_product = "select name, quantity, price, category, discount from products"
    cursor.execute(query_for_product)

    product_data = [(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
    product_name = [row[0] for row in product_data]
    product_quantity = [row[1] for row in product_data]
    product_price = [row[2] for row in product_data]
    product_category = [row[3] for row in product_data]
    product_discount = [row[4] for row in product_data]

    print("S.No \tName \t\tCategory \t\tPrice \t\tQuantity \tDiscount")
    sno = 1

    for i in range(len(product_name)):
        print(str(sno) + "\t" + str(product_name[i]) + "\t\t" + str(product_category[i]) + "\t\t\t" 
            + str(product_price[i]) + "\t\t" + str(product_quantity[i]) + "\t\t" + str(product_discount[i]))
        sno += 1

def value():
    global final_amount
    while True:
        return final_amount

if __name__ == "__main__":
    while True:
        create_bill()
        ques = input("Do you want to create more bill?(Y/n) ").lower().strip()
        if ques == 'y':
            clear_terminal()

        else:
            break