from sqlalchemy.orm import Session
from model import CadastroModel
from schemas import CadastroSchema
import uuid


def create_user(db: Session, cadastro: CadastroSchema):
    _cadastro = CadastroModel(id=str(uuid.uuid4()), name=cadastro.nome, email=cadastro.email,senha=cadastro.senha)
    db.add(_cadastro)
    db.commit()
    db.refresh(_cadastro)
    return _cadastro


def get_users(db: Session, skip: int = 0, limit: int = 30):
    return db.query(CadastroModel).offset(skip).limit(limit).all()
