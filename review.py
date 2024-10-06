import mysql.connector


def createConn():
    global conn
    global cursor

    conn = mysql.connector.connect(
        host='localhost', password='sumanjeet83', user='root', database='shop')
    cursor = conn.cursor()


def see_all_review():
    global conn
    global cursor
    createConn()

    query = "select * from reviews"

    cursor.execute(query)

    for (id, name, star, message, date) in cursor:
        print("\nId:\t\t {} \nName:\t\t {}\nStar Rating:\t {} \nMessage:\t {} \nDate:\t\t {}"
            .format(id, name, star, message, date))
        print("-"*75)

    conn.commit()
    cursor.close()
    conn.close()

def see_review_by_id():
    global conn
    global cursor

    while True:
        createConn()

        id = int(input("Enter id: "))

        query = "select * from reviews where (id = '%(id)s')"
        values = {
            'id' : id,
        }

        cursor.execute(query, values)

        for (id, name, star, message, date) in cursor:
            print("\nId:\t\t {} \nName:\t\t {}\nStar Rating:\t {} \nMessage:\t {} \nDate:\t\t {}"
                .format(id, name, star, message, date))

        if cursor.rowcount > 0:
            pass

        else:
            print("\nNo review found!")

        ques = input("Do you want to see other reviews? (y/n)").lower().strip()
        if ques == 'n':
            print("Exiting...")
            break

        cursor.close()
        conn.close()


def average_rating():
    global conn
    global cursor

    createConn()

    query = "select star from reviews"

    cursor.execute(query)
    star_rating = [star[0] for star in cursor]

    sum = 0
    for i in range(len(star_rating)):
        sum += star_rating[i]

    avg = sum/len(star_rating)
    avg_formatted = f"{avg:.2f}"
    print("Average ratings given by customer(out of 5): " + str(avg_formatted))

