from services.book_service import BookService
from services.user_service import UserService

def main():
    print("Welcome to the Library Management System")
    book_service = BookService()
    user_service = UserService()

    while True:
        print("\nMain Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View All Users")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_service.add_book(title, author, isbn)
        elif choice == "2":
            isbn = input("Enter ISBN of the book to remove: ")
            book_service.remove_book(isbn)
        elif choice == "3":
            query = input("Enter book title or author or ISBN: ")
            results = book_service.search_books(query)
            for book in results:
                print(book)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to borrow: ")
            user_service.borrow_book(user_id, isbn)
        elif choice == "5":
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to return: ")
            user_service.return_book(user_id, isbn)
        elif choice == "6":
            users = user_service.get_all_users()
            for user in users:
                print(user)
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
