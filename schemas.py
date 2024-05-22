from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field


T = TypeVar("T")


class CadastroSchema(BaseModel):
    nome: Optional[str] = ''
    email: Optional[str] = ''
    senha: Optional[str] = ''

    class Config:
        from_attributes = True


class Item(BaseModel):
    name: str
    price: float


class Response(Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = ''
