from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#  docker exec -it <id conteiner> psql -U <database> use para acessar o terminar iterativo do postgrees
DATABASE_URL = "postgresql://user:password@localhost:32769"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
