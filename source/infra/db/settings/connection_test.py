import pytest
from sqlalchemy import text
from .connection import DbConnectionHandler


@pytest.mark.skip()
def test_db_connection():
    db_connection_handler = DbConnectionHandler()

    engine = db_connection_handler.get_db_engine()

    conn = engine.connect()
    conn.execute(
        text(
            "CREATE TABLE register_users "
            "(id SERIAL PRIMARY KEY,first_name VARCHAR(100),last_name VARCHAR(100), age INTEGER);")
    )
    conn.commit()
    print(engine)
