# Non-modular Bookstore Inventory System
books = []

def bookInfo():
    for i in range(3):
        title = input(f"Enter title of book {i + 1}: ")
        author = input(f"Enter author of book {i + 1}: ")
        price = float(input(f"Enter price of book {i + 1}: "))
        books.append({"title": title, "author": author, "price": price})

def bookInventory():
    for i, book in enumerate(books, start=1):
        print(f"Book {i}: Title = {book['title']}, Author = {book['author']}, Price = £{book['price']:.2f}")

def totalValue():
    total_value = sum(book["price"] for book in books)
    print(f"\nTotal inventory value: £{total_value:.2f}")



book_info = bookInfo()
book_inventory = bookInventory()
total_value = totalValue()