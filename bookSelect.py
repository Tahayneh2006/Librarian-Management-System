import matplotlib.pyplot as plt
import database as db

# Import the required modules

def generate_recommendations():

    # 1. Create two lists. One holds Book Info, other holds Library Logs.
    books = db.read_books()
    logs = db.read_logs()

    # 2. Create 2 dictionaries. One holds the counts for each book,
    #    other holds the counts of each genre.
    books_count = {book["ID"]: 0 for book in books}
    genre_count = {}

    # 3. Loop through the contents of the Library Logs list.
    for log in logs:
        # 4. During each iteration, assign the ID found in the Library Logs list to the temporary variable.
        book_id = log["Book ID"]

        # 5. Increment the count in the books_count dictionary.
        if book_id in books_count:
            books_count[book_id] += 1

        # 6. Inner loop to loop through the contents of the Book Info list.
        for book in books:
            if book["ID"] == book_id:
                genre = book["Genre"]

                # 7. Add the genre to the genre_count dictionary if it's not there.
                #    Else increment the count.
                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1
                break # -> Exit the inner loop

    # 8. Take each dictionary and compare the VALUES not KEYS. (if second arg is missing, the function would compare     keys.)
    pop_genre = max(genre_count, key=genre_count.get)
    pop_book = max(books_count, key=books_count.get)

    # 9. Accept user input, remove spaces.
    annual_budget = input("Enter the annual budget: ").strip()

    # 10. Attempt to cast the String into a Float.
    try:
        annual_budget = float(annual_budget)

    # 11. If casting fails, print the following error message.
    except ValueError:
        print("Invalid input. Input must be numbers.")

    # 12. If casting succeeds, proceed to the following else code block.
    else:

        price = 0
        title = ""

        # 13. Loop through the contents of the Book Info list.
        for book in books:
            # 14. Find the most popular book and get its ID and title, then exit.
            if book['ID'] == pop_book:
                price = book['PurchasePrice']
                title = book['Title']
                break

        # 15. Check if given budget is not zero or a negative number AND the same with book price
        if annual_budget > 0 and price > 0:
            # 16. Integer divison.
            num_copies = int(annual_budget // price)
            # 17. Generate the recommendation list.
            print("\n--- RECOMMENDATION ---")
            print(f"Most Popular Genre: {pop_genre}")
            print(f"Most Popular Book: {title}")
            print(f"Cost per copy: ${price}")
            print(f"With a budget of ${annual_budget:.2f}, you can purchase {num_copies} more copies.\n")

        else:
            print("Invalid price")



def visualize():

    # 1. Create two lists. One holds Book Info, other holds Library Logs.
    books = db.read_books()
    logs = db.read_logs()

    # 2. Create 2 dictionaries. One holds the counts for each book,
    #    other holds the counts of each genre.
    books_count = {book["ID"]: 0 for book in books}
    genre_count = {}

    # 3. Loop through the contents of the Library Logs list.
    for log in logs:
        # 4. During each iteration, assign the ID found in the Library Logs list to the temporary variable.
        book_id = log["Book ID"]

        # 5. Increment the count in the books_count dictionary.
        if book_id in books_count:
            books_count[book_id] += 1

        # 6. Inner loop to loop through the contents of the Book Info list.
        for book in books:

            if book["ID"] == book_id:
                genre = book["Genre"]
                # 7. Add the genre to the genre_count dictionary if it's not there.
                #    Else increment the count.
                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1
                break # -> Exit the inner loop


    # 8. Create an inner sub-menu.
    print("\n--- VISUALIZATION MENU ---")
    print("1. Book Popularity (Bar Chart)")
    print("2. Genre Distribution (Pie Chart)")
    choice = input("Select a chart (1 or 2): ").strip()

    match choice:
        case "1":
            # 9. Create a dictionary to sum counts.
            title_counts = {}

            # 10. Loop through the contents of the books_count dictionary and get each key and value.
            for b_id, count in books_count.items():

                # 11. Only get the books that have been loaned at least ONCE.
                if count > 0:
                    # 12. Inner loop to loop the Book Info list.
                    for book in books:
                        if book["ID"] == b_id:
                            title = book["Title"]

                            # 13. If title exists, add to existing count. If not, create it.
                            if title in title_counts:
                                title_counts[title] += count
                            else:
                                title_counts[title] = count
                            break # -> Exit the inner loop

            # 14. Prepare lists from the title_count dictionary.
            titles_y = list(title_counts.keys())
            counts_x = list(title_counts.values())

            # 15. Create a HORIZONTAL bar chart, the X-axis holds the count, the Y-Axis holds the title.
            plt.barh(titles_y, counts_x, edgecolor="black")
            # 16. Name the X-axis and Y-Axis label, and add a title to the bar chart.
            plt.xlabel("Total Loans")
            plt.ylabel("Book Title")
            plt.title("Book Popularity")

            plt.tight_layout() # -> Used so that text doesn't overlap
            plt.locator_params(integer=True) # -> Changes the count in the
            plt.show() # -> Shows the bar chart

        case "2":
            # 17. Prepare lists from the genre_count dictionary.
            genres = list(genre_count.keys())
            counts = list(genre_count.values())

            plt.pie(counts, labels=genres,explode= [0.05] * len(counts), autopct='%1.1f%%' ,shadow=True)
            plt.title("Most Popular Genres")
            plt.show()

        case _: # -> Default case (Invalid input)
            print("Invalid choice. Going back to the main menu.")


