from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_engine(db_url: str) -> Engine:
    if not db_url:
        raise ValueError("Database URL cannot be empty")

    return create_engine(
        db_url,
        pool_pre_ping=True,
        future=True,
    )

