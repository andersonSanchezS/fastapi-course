from fastapi import FastAPI
#from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID
app = FastAPI()

class book(BaseModel):
    id: UUID
    title: str       = Field(min_length=1, max_length=100, title="Title of the book")
    author: str      = Field(min_length=1, max_length=100, title="Author of the book")
    description: Optional[str] = Field(min_length=1, max_length=1000, title="Description of the book")
    rating: int      = Field(gt=-1, lt=101, title="Rating of the book")

books = []

@app.get("/")
def getBooks():
    return {"data": books}

@app.post("/books")
def addBook(book: book):
    books.append(book)
    return {"message": "Book added successfully"}

'''
books = {
    'book_1': {'id': '01b51f37-7b6a-4abc-a6ce-64b2a18750fd', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    'book_2': {'id': 'e7c4b298-41ed-4f11-9f66-7a2091f3152a', 'title': 'The Catcher in the Rye', 'author': 'J. D. Salinger'},
    'book_3': {'id': 'bc94a9f9-6e63-4f8d-93c1-11f02b4d6597', 'title': 'The Grapes of Wrath', 'author': 'John Steinbeck'},
    'book_4': {'id': '984db03e-da1b-41a1-9729-c5e20088754f', 'title': 'The Sun Also Rises', 'author': 'Ernest Hemingway'},
    'book_5': {'id': '98395dd9-251a-4641-bc0f-9ac22ad1c33e', 'title': 'The Lord Of The Rings', 'author': 'J. R. R. Tolkien'},
}

class directionName(str, Enum):
    asc = 'asc'
    desc = 'desc'


@app.get("/books/list")
async def getBooks():
    return {"data": books}

@app.get("/books/{id}")
async def getBook(book_id: Optional[str]):
    return {"data": books[book_id]}

@app.post("/books/create")
async def createBook(book: dict):
    books[book['id']] = book
    return {"data": books[book['id']]}

@app.put("/books/update/{id}")
async def updateBook(book_id: str, book: dict):
    books[book_id] = book
    return {"data": books[book_id]}

@app.delete("/books/delete/{id}")
async def deleteBook(book_id: str):
    del books[book_id]
    return {"data": "Book deleted"}

@app.get("/books/sort/{direction}") 
async def sortBooks(direction: directionName):
    if direction == 'asc':
        return {"data": sorted(books, key=lambda x: books[x]['title'])}
    else:
        return {"data": sorted(books, key=lambda x: books[x]['title'], reverse=True)}
'''