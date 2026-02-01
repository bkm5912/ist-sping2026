# define the large library as a list
library = []

def show_menu():
    """
    Display the main menu options to the user
    """

    print("\nPersonal Library Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Update a book")
    print("4. List all books")
    print("5. Search for a book")
    print("6. Show stats")
    print("7. Exit")


def add_book():
    # ask the user for some info
    title = input("\nEnter the title of the book: ").strip()
    author = input("Enter the author's name: ").strip()
    year_published = input("Enter the year the book was published: ").strip()
    print(f"Added: {title}")

    # create the dictionary for a single book
    book = {"title": title, "author": author, "year_published": year_published}

    # add it to the large library
    library.append(book)
    print(library) # testing


def remove_book():
    # ask the user for what book to remove
    book_to_remove = input("Enter the title of the book to remove: ").strip()
    # search through each book in the library
    for book in library:
        if book["title"].lower() == book_to_remove.lower():
            library.remove(book)
            print(f"Removed: {book_to_remove}")
            print(library) # testing
            # exits the function if a match is found
            return
    # if no match is found, print an error
    print("Book not found")


def update_book():
    # must be case insensitive, so make it lowercase
    book_to_update = input("\nEnter the name of the book to update: ").lower().strip()
    for book in library:
        if book["title"].lower() == book_to_update:
            print("1. Title")
            print("2. Author")
            print("3. Publication Date")
            choice = input("\nWhat do you want to update? ").strip()
            if choice == "1":
                book["title"] = input("Enter the new title: ")
                print(library) # testing
            elif choice == "2":
                book["author"] = input("Enter the new author: ")
                print(library) # testing
            elif choice == "3":
                book["year_published"] = input("Enter the new publication date: ")
                print(library) # testing
            return
    print("Book not found")


def list_all_books():
    count = 0
    print("Here are all the books in your library:")
    for book in library:
        count += 1
        print(f"{count}. {book["title"]}")


def search():
    # must be case insensitive
    search = input("What book would you like to search for? ").lower().strip()
    for book in library:
        # partial matches, so I use "in" and not == like I did for updating a book
        if search in book["title"].lower():
            print(f"Here's what was found: {book["title"]} by {book["author"]}, published in {book["year_published"]}")
            return
    print("No matches found")


def show_stats():
    pass


def main():
    """
    Main function that loops the menu options
    """

    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            list_all_books()
        elif choice == "5":
            search()
        elif choice == "6":
            show_stats()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()