import bill, main_menu


def options():
    try:
        print("NOTE - for online payment with qrcode, run website.py manually")
        print("1) Create Bill")
        print("2) See products")
        print("99) Logout (redirected to login page)")
        opt = int(input("Select Option: "))

        if opt == 1:
            bill.create_bill()

        elif opt == 2:
            bill.see_products()

        elif opt == 99:
            main_menu.clear_terminal()
            main_menu.main()

        else:
            print("Invalid option...")


    except Exception as e:
        print("Error occurred: ", e)