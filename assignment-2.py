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
    print("6. Exit")


def add_book(library: list[str] = []):
    title = input("Enter the title of the book: ").strip()
    library.append(title)
    print(f"Added: {title}")

def remove_book():
    pass

def update_book():
    pass

def main():
    """
    Main function that loops the menu options
    """

    library: list[str] = [] # initialized to be empty


    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book()
        elif choice == "3":
            update_book()


        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")







if __name__ == "__main__":
    main()