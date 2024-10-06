import for_product, for_customer, for_sales, for_review, for_bill
def menu():
    try:
        while True:
            print("\n\n------Welcome------")
            print("---Select option---")
            print()
            print("1) Products")
            print("2) Customer")
            print("3) Sales")
            print("4) Reviews")
            print("5) Billing")
            print("6) Server")
            opt = int(input("\nSelect the option for what you want to see or make change: "))

            if opt == 1:
                for_product.options()

            elif opt == 2:
                for_customer.options()

            elif opt == 3:
                for_sales.options()

            elif opt == 4:
                for_review.options()

            elif opt == 5:
                for_bill.options()

            elif opt == 6:
                print("Note: Please run server file manually...")

            else:
                print("Invalid Option...\n")

    except Exception as e:
        print("Error occurred: ", e)


