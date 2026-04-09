import database as db

# Import required module

def search_books():

    # 1. Create two lists. One holds Book Info, other holds Library Logs.
    logs = db.read_logs()
    books = db.read_books()

    is_found = False # <- Assume book is not found

    # 2. Accept user input, turn it into lowercase and remove all spaces.
    user_input = input("\nEnter book title: ").lower().strip()

    # 3. Loop through the contents of the book info list.
    for book in books:
        # 4. For every title check if it's equal to the provided user input.
        if book["Title"].lower() == user_input:
            # 5. Store the ID in a temporary variable.
            current_id = book["ID"]
            is_found = True
            # 6. Assume that the book is available. (Not on loan)
            is_available = True

            # 7. Loop through the contents of the logs list.
            for log in logs:
                # 8. Check whether if the book is available or is taken.
                if log["Book ID"] == current_id and log["Return Date"] == "0":
                    is_available = False
            status = "Available" if is_available else "On Loan"

            # 9. Print book status.
            # (Note: There could be 2 books of the same title with different IDs.)
            print("=====================")
            print(f"ID: {book['ID']}\nTitle: {book['Title']}\nAuthor: {book['Author']}\nStatus: {status}")
            print("=====================")

    # 10. If book was not found (e.g. Probably invalid input), We print this message.
    if not is_found:
        print("Book not found")






