def read_books():

    # 1. Create an empty list.
    books = []

    # 2. Read the Book_Info file using with open()
    with open("Book_Info.txt", "r") as file:
        # 3. Skip the headers.
        next(file)
        # 4. Loop through the contents of the file
        for data in file:

            # 5. Remove the newline character, then remove the commas, and return
            #    each row as a list.   (e.g. ['1','Sci-Fi','Dune','Frank Herbert','15,01/01/2020'])
            data = data.strip().split(",")

            # 6. Convert each list into a dictionary for better readability and easier access.
            #    (e.g. ['1','Sci-Fi','Dune','Frank Herbert','15,01/01/2020'] -> {'ID': 1, 'Genre': 'Sci-Fi'...})

            current_book = {
                "ID": int(data[0]),
                "Genre": data[1],
                "Title": data[2],
                "Author": data[3],
                "PurchasePrice": float(data[4]), # -> Price may include floating point decimals.
                "PurchaseDate": data[5]
            }

            # 7. Add this to our list.
            books.append(current_book)

    # 8. Return the list.
    return books

def read_logs():

    # 1. Create an empty list.
    logs = []
    # 2. Read the logfile file using with open()

    with open("logfile.txt", "r") as file:
        # 3. Skip the headers.
        next(file)

        # 4. Loop through the contents of the file
        for log in file:

            # 5. Remove the newline character, then remove the commas, and return
            log = log.strip().split(",")

            # 6. Convert each list into a dictionary for better readability and easier access.

            current_log = {
                "Book ID": int(log[0]),
                "Member ID": int(log[1]),
                "Checkout Date": log[2],
                "Return Date": log[3],
                "Reserved ID": int(log[4])
            }
            # 7. Append the dictionary to the list.
            logs.append(current_log)

    # 8. Return the list.
    return logs

def reserve_book(book_id, member_id):

    # 1. Create a list which holds the Library Logs.
    logs = read_logs()

    reservation_success = False

    # 2. Loop through the contents of the list.
    for log in logs:

        # 3. Check if the Book is in the logfile and has not been returned yet.
        # (log["Return Date"] == "0" means the book hasn't been returned yet.)
        if book_id == log["Book ID"] and log["Return Date"] == "0":

            # 4. If this is true, then the book has been already reserved by someone else.
            if log["Reserved ID"] != 0:
                print("Book is already reserved by someone else.\n")

                # 5. Break out of the loop.
                break

            # 6. If the book has not been reserved yet (Reserved ID = 0)
            #    then it we reserve it for the Member ID provided from the checkout_books() function.
            else:
                log["Reserved ID"] = member_id
                # 7. Change the status to True.
                reservation_success = True
                # 8. Break out of the loop.
                break

    if reservation_success:
        # 9. Overwrite the file.
        with open("logfile.txt", "w") as file:
            # 10. Add the top headers.
            file.write("BookID,MemberID,CheckoutDate,ReturnDate,ReservedID\n")
            # 11. Loop through the list contents.
            for log in logs:
                # 12. Re-write the file with the new changes
                # (Reserved ID for the specific book is changed to the given Member ID.)
                file.write(f"{log['Book ID']},{log['Member ID']},{log['Checkout Date']},{log['Return Date']},{log['Reserved ID']}\n")
        return True
    return False

