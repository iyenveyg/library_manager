from library_manager.book_manager import BookManager

def main():
    book_manager = BookManager()

    while True:
        print("\nLibrary Manager")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Change Book Status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter year: "))
            book_manager.add_book(title, author, year)
            print("Book added successfully.")

        elif choice == '2':
            book_id = int(input("Enter book ID to delete: "))
            book_manager.delete_book(book_id)
            print("Book deleted successfully.")

        elif choice == '3':
            title = input("Enter title (or press Enter to skip): ")
            author = input("Enter author (or press Enter to skip): ")
            year = input("Enter year (or press Enter to skip): ")
            year = int(year) if year else None
            results = book_manager.search_books(title, author, year)
            for book in results:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")

        elif choice == '4':
            book_manager.display_books()

        elif choice == '5':
            book_id = int(input("Enter book ID to change status: "))
            new_status = input("Enter new status ('в наличии' or 'выдана'): ")
            book_manager.change_book_status(book_id, new_status)
            print("Book status changed successfully.")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
