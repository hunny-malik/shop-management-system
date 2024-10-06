import mysql.connector


def createConn():
    global conn
    global cursor

    conn = mysql.connector.connect(
        host='localhost', password='sumanjeet83', user='root', database='shop')
    cursor = conn.cursor()


def see_all_sales():
    global conn
    global cursor
    createConn()

    query = ("select * from sales")

    cursor.execute(query)

    for (id, name, phone, total_without_gst, total_with_gst, date) in cursor:
        print("Id:\t\t\t {} \nName:\t\t\t {} \nTotal(without gst):\t {} \nTotal(with gst):\t {} \nDate:\t\t\t {}"
            .format(id, name, total_without_gst, total_with_gst, date))
        print("-"*75)

    conn.commit()
    cursor.close()
    conn.close()


def see_sales_by_id():
    global conn
    global cursor

    while True:
        createConn()

        query = ("select * from sales where (id='%(id)s')")

        i = int(input("\nEnter id: "))

        values = {
            'id': i,
        }

        cursor.execute(query, values)

        for (id, name, phone, total_without_gst, total_with_gst, date) in cursor:
            print("Id:\t\t\t {} \nName:\t\t\t {} \nTotal(without gst):\t {} \nTotal(with gst):\t {} \nDate:\t\t\t {}"
                .format(id, name, total_without_gst, total_with_gst, date))

        if cursor.rowcount > 0:
            pass

        else:
            print("\nNo sales found!")

        ques = input("Do you want to see other sales? (y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break

        cursor.close()
        conn.close()


def total_sales():
    global conn
    global cursor
    createConn()

    query = "select total_without_gst, total_with_gst from sales"

    cursor.execute(query)
    result_set = cursor.fetchall()  

    total_without_gst_output = [row[0] for row in result_set]
    total_with_gst_output = [row[1] for row in result_set]

    sum_without_gst = sum(total_without_gst_output)
    sum_with_gst = sum(total_with_gst_output)

    print("Sum of sales(without gst):\t", sum_without_gst)
    print("Sum of sales(with gst):\t\t", sum_with_gst)

    conn.close()
    cursor.close()

