def store_unique(book_list):
    unique_books = set(book_list)   
    return unique_books
book_ids = []
n = int(input("Enter number of book IDs: "))
for i in range(n):
    bid = input(f"Enter book ID {i+1}: ")
    book_ids.append(bid)
unique_ids = store_unique(book_ids)
print("\nOriginal list of book IDs:", book_ids)
print("Unique book IDs stored in a set:", unique_ids)