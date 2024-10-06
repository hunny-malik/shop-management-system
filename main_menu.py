import pwinput, os
import owner, cashier, customer_manager, financier, overall_manager, product_manager, reviewer

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        print("-------WELCOME-------")
        username = input("Enter Username: ")
        password = pwinput.pwinput(prompt= "Enter Password: ")

        if username == 'owner' and password == 'owner':
            owner.menu()

        elif username == 'cashier' and password == 'cashier':
            cashier.menu()

        elif username == 'c manager' and password == 'c manager':
            customer_manager.menu()

        elif username == 'financier' and password == 'financier':
            financier.menu()

        elif username == 'o manager' and password == 'o manager':
            overall_manager.menu()

        elif username == 'p manager' and password == 'p manager':
            product_manager.menu()

        elif username == 'reviewer' and password == 'reviewer':
            reviewer.menu()

        else:
            print("Incorrect Username or Password...")

    except Exception as e:
        print("Error occurred: ", e)