import database as db
from datetime import datetime

# Import required modules

def checkout_books():

    # 1. Create two lists. One holds Book Info, other holds Library Logs.
    books = db.read_books()
    logs = db.read_logs()

    # 2. Accept user input, remove spaces.
    member_id = input("Enter Member ID (4 digits): ").strip()

    # 3. Check if the amount of characters is equal to 4.
    if len(member_id) != 4:
        print("Member ID must be exactly 4 digits.")
        return # -> This means do not continue and exit the function.

    # 4. Attempt to cast the string into an Integer.
    try:
        member_id = int(member_id)

    # 5. If one or more characters of the String are not digits,
    # print the following error message.
    except ValueError:
        print("Invalid ID format. ID must be only numbers.")

    # 6. If member ID was valid and is 4 digits long, proceed with the else block of code.
    else:

        # 7. Accept user input, remove spaces.
        book_id = input("Enter Book ID (1-25): ").strip()

        # 8. Attempt to cast the String into an Integer.
        try:
            book_id = int(book_id)

        # 9. If casting failed, print the following error message.
        except ValueError:
            print("Invalid ID format. ID must be only numbers\n")

        # 10. If input was valid, proceed with the else block of code.
        else:
            # 11. Assume book is not in the Book Info file.
            book_exists = False
            is_available = True
            # 12. Loop through the contents of the Book Info list.
            for book in books:
                # 13. If user input is the same as the book ID in the book info list.
                #     We change the status to True.
                if book["ID"] == book_id:
                    book_exists = True

                    # 14. Inner loop to loop through the Library Logs list.
                    for log in logs:
                        # 15. Check if book is available or not.
                        #     (log["Return Date"] = "0" means book hasn't been returned.)
                        if book_id == log["Book ID"] and log["Return Date"] == "0":
                            is_available = False
                            break

            # 16. Exit function if the book was not found in the Book Info file.
            if not book_exists:
                print(f"Book not found in library")
                return

            elif not is_available:
                # 17. Provide the choice to reserve the book or not.
                print("Book is currently on loan")
                choice = input("Would you like to reserve it (Y/N)?: ").upper()
                match choice:
                    case "Y":
                        if db.reserve_book(book_id, member_id): # -> This function returns true or false.
                            print(f"Book {book_id} reserved for Member {member_id}\n") # -> Go to reserve_book() function in database.py
                        else:
                            print("Reservation failed.\n")
                    case "N":
                        print("Reservation declined.\n")
                # 18. If input was not Y or N, print the following message.
                    case _:
                        print("Invalid choice\n")

            # 19. If book exists and is available, check it out to the given Member ID.
            else:
                # 20. Create a timestamp format of the following: (Year-Month-Day)
                timestamp_format = "%Y-%m-%d"
                # 21. Get the current time.
                now = datetime.now()
                # 22. Format the current time.
                timestamp = now.strftime(timestamp_format)


                with open("logfile.txt", "a") as file:
                    # 23. Append the new information to our logfile.
                    file.write(f"{book_id},{member_id},{timestamp},0,0\n")
                    # 24. Print success message.
                    print(f"Book {book_id} is available! Checkout processed for {member_id} at {timestamp}\n")