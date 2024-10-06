import customer, main_menu

def options():
    try:
        print("1) Add Customer")
        print("2) See Customer")
        print("3) Update Customer full info")
        print("4) Search Customer")
        print("5) Delete Customer")
        print("99) Logout (redirected to Login page)")
        opt = int(input("Select option: "))

        if opt == 1:
            customer.add_customer()

        elif opt == 2:
            print("1) All Customer")
            print("2) By ID")
            opt_for_see = int(input("Select option: "))
            if opt_for_see == 1:
                customer.show_all_customers()

            elif opt_for_see == 2:
                customer.show_customer_by_id()

            else:
                print("Invalid option...")

        elif opt == 3:
            customer.update_customer_full_info()

        elif opt == 4:
            customer.search_customer()

        elif opt == 5:
            customer.delete_customers()

        elif opt == 99:
            main_menu.clear_terminal()
            main_menu.main()

        else:
            print("Invalid option...")

    except Exception as e:
        print("Error occurred: ", e)


