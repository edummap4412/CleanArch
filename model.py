from sqlalchemy import Column, Integer, String
from config import Base


class CadastroModel(Base):
    __tablename__ = 'cadastro'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    senha = Column(String)
