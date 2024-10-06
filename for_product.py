import product, main_menu

def options():
    try:
        print("1) Add Product")
        print("2) See Product")
        print("3) Update Product")
        print("4) Search Product")
        print("5) Delete Product")
        print("99) Logout (redirected to Login page)")
        opt = int(input("Select option: "))

        if opt == 1:
            product.add_product()

        elif opt == 2:
            print("1) All Products")
            print("2) By ID")
            opt_for_prd = int(input("Select option: "))
            if opt_for_prd == 1:
                product.show_all_products()

            elif opt_for_prd == 2:
                product.show_product_by_id()

            else:
                print("Invalid option...")

        elif opt == 3:
            print("1) All info")
            print("2) Quantity")
            print("3) Price")
            opt_for_upd = int(input("Select option: "))
            if opt_for_upd == 1:
                product.update_product_full_info()

            elif opt_for_upd == 2:
                product.update_product_quantity()

            elif opt_for_upd == 3:
                product.update_product_price()

            else:
                print("Invalid option...")

        elif opt == 4:
            product.search_product()

        elif opt == 5:
            product.delete_product()

        elif opt == 99:
            main_menu.clear_terminal()
            main_menu.main()

        else:
            print("Invalid option...")

    except Exception as e:
        print("Error occurred: ", e)


