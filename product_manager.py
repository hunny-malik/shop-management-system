import for_product
def menu():
    try:
        while True:
            print("\n\n------Welcome------")
            for_product.options()

    except Exception as e:
        print("Error occurred: ", e)