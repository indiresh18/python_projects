list_of_books = []
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        
def admin():
    print("Welcome to the Admin Panel.")
    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Logout")
        admin_choice = input("Enter your choice: ")
        if admin_choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            new_book = Book(title, author)
            list_of_books.append(new_book)
            print(f"Book '{title}' by {author} added successfully.")
        elif admin_choice == '2':
            print("Removing a book...")
            name = input("Enter the title of the book to remove: ")
            for book in list_of_books:
                if book.title == name:
                    list_of_books.remove(book)
                    print(f"Book '{name}' removed successfully.")
                else:
                    print(f"Book '{name}' not found.")
        elif admin_choice == '3':
            print("Viewing books...")
            for book in list_of_books:
                print(f"- {book.title} by {book.author}")
        elif admin_choice == '4':
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")
    
def user():
    print("Welcome to the User Panel.")
    while True:
        print("1.view Books")
        print("2.Get book to read")
        print("3.return book")
        print("4.Logout")
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            print("Viewing books...")
            for book in list_of_books:
                print(f"- {book.title} by {book.author}")
        elif user_choice == '2':
            print("Getting a book to read...")
            name = input("Enter the title of the book you want to read: ")
            for book in list_of_books:
                if book.title.lower()== name.lower():
                    print(f"You have borrowed '{name}' by {book.author}. Enjoy reading!")
                    print("NOTE :Please return the book after reading, You have 7 days to return the book.")
                    print("If you don't return the book within 7 days, you will be fined $5 per day.")
                    
                    list_of_books.remove(book)
                    return
            else:
                print(f"Book '{name}' not found.")
        elif user_choice == '3':
            print("Returning a book...")
            name = input("Enter the title of the book you want to return: ")
            author = input("Enter the author of the book: ")
            return_date=input("HOW MANY DAYS DID YOU KEEP THE BOOK? : ")
            if int(return_date) > 7:
                fine = (int(return_date) - 7) * 5
                print(f"You have a fine of ${fine} for returning the book late.")
            else:
                print("Thank you for returning the book on time.")
            
            print(f"You have returned '{name}'. Thank you!")
            book = Book(name, author)  
            list_of_books.append(book)        
        elif user_choice == '4':
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")
    
print("-----------------LIBRARY---------------")
while True:
    print("SELECT YOUR CATEGORY")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        admin()
    elif choice == '2':
        user()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        
        
        
        
        
