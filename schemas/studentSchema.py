from pydantic import BaseModel
from typing import Optional


# Student Schema for POST_API
class Address(BaseModel):
    city: str
    country: str


class StudentModel(BaseModel):
    name: str
    age: int
    address: Address


# Student Schema for Update the Student [PATCH API]
class PatchAddress(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None


class PatchStudentModel(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[PatchAddress] = None

