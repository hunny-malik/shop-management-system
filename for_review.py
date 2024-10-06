import review, main_menu
def options():
    try:
        print("1) See Reviews")
        print("2) Average Ratings")
        print("99) Logout (redirected to Login page)")
        opt = int(input("Select Option: "))
        if opt == 1:
            print("1) All Reviews")
            print("2) By ID")
            opt_for_rev = int(input("Select options: "))
            if opt_for_rev == 1:
                review.see_all_review()

            elif opt_for_rev == 2:
                review.see_review_by_id()

            else:
                print("Invalid Option...")

        elif opt == 2:
            review.average_rating()

        elif opt == 99:
            main_menu.clear_terminal()
            main_menu.main()

        else:
            print("Invalid Option...")

    except Exception as e:
        print("Error occurred:", e)