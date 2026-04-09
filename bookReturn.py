import database as db
from datetime import datetime

# Import required modules

def return_book():

    # 1. Accept user input, remove spaces.
    book_id = input("Enter Book ID: ").strip()

    # 2. Attempt to cast the String into an Integers.
    try:
        book_id = int(book_id)

    # 3. If casting failed, print the following error message.
    except ValueError:
        print("Invalid ID format. ID must be only numbers.")

    # 4. If casting succeeded, proceed to the following else code block.
    else:
        # 5. Create a timestamp format of the following: (Year-Month-Day)
        timestamp_format = "%Y-%m-%d"
        # 6. Get the current time.
        now = datetime.now()
        # 7. Format the current time.
        timestamp = now.strftime(timestamp_format)
        found_loan = False
        new_reservation = ""
        reserver_id = -1
        # 8. Create a list which holds the Library Logs.
        logs = db.read_logs()

        # 9. Loop through the contents of the list.
        for log in logs:
            # 10. Check if book is currently on loan or not.
            if book_id == log["Book ID"] and log["Return Date"] == "0":
                found_loan = True
                # 11. Store the ID of the member who reserved the book. (Or 0 if it wasn't reserved)
                reserver_id = log["Reserved ID"]
                # 12. Modify the return date to the current timestamp.
                log["Return Date"] = timestamp

                # 13. If the book was reserved by someone else, immediately check it out for the reserver.
                if reserver_id != 0:
                    print(f"Book {book_id} returned. Reservation found for Member {reserver_id}.")
                    print("Processing automatic checkout...\n")
                    new_reservation = f"{book_id},{reserver_id},{timestamp},0,0\n"
                else:
                    print(f"Book {book_id} has been returned and is available for checkout.")
                break # -> Exit the loop when we process the book return.

        # 14. If the book was not on loan, print the following message and exit the function.
        if not found_loan:
            print("Book is not currently on loan")
            return

        else:
            # 15. Overwrite the logfile File.
            with open("logfile.txt", "w") as file:
                # 16. Add the headers to the top.
                file.write("BookID,MemberID,CheckoutDate,ReturnDate,ReservedID\n")
                for log in logs:
                    # 17. Rewrite the logs.
                    file.write(f"{log['Book ID']},{log['Member ID']},{log['Checkout Date']},{log['Return Date']},{log['Reserved ID']}\n")

                if new_reservation != "":
                    # 18. Add the new information.
                    file.write(new_reservation)
                    print(f"Book automatically been checked out to Member {reserver_id}\n")



