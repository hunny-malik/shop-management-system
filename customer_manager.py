import for_customer
def menu():
    try:
        while True:
            print("\n\n------Welcome------")
            for_customer.options()


    except Exception as e:
        print("Error occurred: ", e)