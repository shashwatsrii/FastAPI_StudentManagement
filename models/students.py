# models/students.py
from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class StudentList(BaseModel):
    data: list[Student]

class StudentQueryParams(BaseModel):
    country: Optional[str] = None
    age: Optional[int] = None

class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]