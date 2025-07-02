from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic model for input validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

# Fake database
books_db: List[Book] = []