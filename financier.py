import for_sales
def menu():
    try:
        while True:
            print("\n\n------Welcome------")
            for_sales.options()

    except Exception as e:
        print("Error occurred: ", e)