import sales, main_menu
def options():
    try:
        print("1) See Sales")
        print("2) Total Sales")
        print("99) Logout (redirected to Login page)")
        opt = int(input("Select Option: "))
        if opt == 1:
            print("1) All Sales")
            print("2) By ID")
            opt_for_sale = int(input("Select options: "))
            if opt_for_sale == 1:
                sales.see_all_sales()

            elif opt_for_sale == 2:
                sales.see_sales_by_id()

            else:
                print("Invalid Option...")

        elif opt == 2:
            sales.total_sales()

        elif opt == 99:
            main_menu.clear_terminal()
            main_menu.main()

        else:
            print("Invalid Option...")

    except Exception as e:
        print("Error occurred:", e)