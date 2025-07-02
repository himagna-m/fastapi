from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from db import Book, books_db

app = FastAPI()

books = books_db

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book)
    print('book is :', book.id)
    with open('books.txt', 'a') as f:
        f.write(f"""'the book is ', {book.author}, {book.description}""")
    return book

@app.get("/books/", response_model=List[Book])
def get_all_books(skip: int = 0, limit: int = 10):
    return books[skip:skip+limit]

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

if __name__=="__main__":
    print("books available: ", books)

