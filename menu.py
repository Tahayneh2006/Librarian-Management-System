import bookSearch, bookCheckout, bookReturn, bookSelect


def main_menu():

    print("===============================")
    print("LIBRARIAN MANAGEMENT SYSTEM 1.0")
    print("===============================")

    is_running = True

    while is_running:

        print("\n1. Search for a Book")
        print("2. Book Checkout")
        print("3. Book Return")
        print("4. Library Analytics")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        match choice: # -> Match statement is like the switch statement in Java. Used for better readability

            case "1":
                bookSearch.search_books()

            case "2":
                bookCheckout.checkout_books()

            case "3":
                bookReturn.return_book()

            case "4":

                print("1. Generate Book recommendations")
                print("2. Open Visualization Menu")

                choice = input("\nEnter your choice: ")

                match choice:
                    case "1":
                        bookSelect.generate_recommendations()
                    case "2":
                        bookSelect.visualize()
                    case _:
                        print("Invalid choice. Going back to the main menu.\n")

            case "5":
                    is_running = False

            case _: # -> Default case (Invalid input)
                print("Invalid choice. Please select (1-5)\n")



main_menu()


print("\nThank you for using our latest version of the library management system")