import for_bill
def menu():
    try:
        while True:
            print("\n\n------Welcome------")
            for_bill.options()


    except Exception as e:
        print("Error occurred: ", e)