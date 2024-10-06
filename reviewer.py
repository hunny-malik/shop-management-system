import for_review
def menu():
    try:
        while True:
            print("\n\n------Welcome------")
            for_review.options()

    except Exception as e:
        print("Error occurred: ", e)