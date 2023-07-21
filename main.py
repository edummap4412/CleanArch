from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from schemas import CadastroSchema
from config import SessionLocal
from sqlalchemy.orm import Session
import crud

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"]
)
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def Home():
    return "Welcome Home"


@router.post('/registro')
async def create(request: CadastroSchema, db: Session = Depends(get_db)):
    crud.create_user(db, request)
    return {'data': "CRIADO COM SUCESSO"}


@router.get('/list')
async def list(db: Session = Depends(get_db)):
    _users = crud.get_users(db, 0, 20)
    return _users


@router.delete('/delete{id}')
async def delete(db: Session = Depends(get_db)):
    return


@app.post("/items")
async def create_item(item: CadastroSchema):
    # Lógica para criar o item no banco de dados ou executar outras operações
    return {"message": "Item created successfully", "item": item}

app.include_router(router, prefix='/users')
