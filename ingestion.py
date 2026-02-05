import re
import pandas as pd
from sqlalchemy.engine import Connection

from utils.log_config import get_logger

logger = get_logger("ingestion")


def _clean_table_name(name: str) -> str:
    return re.sub(r"[^\w]+", "_", name.lower().strip())


def ingest_db(
    df: pd.DataFrame,
    table_name: str,
    conn: Connection,
) -> None:
    """
    Create table if not exists, otherwise append data.
    """

    table_name = _clean_table_name(table_name)

    try:
        df.to_sql(
            name=table_name,
            con=conn,
            if_exists="append",   # 👈 THIS IS THE KEY
            index=False,
            chunksize=10_000,
            method="multi",
        )

        logger.info(
            f"Appended {len(df)} rows into '{table_name}'"
        )

    except Exception:
        logger.exception(f"Failed loading table '{table_name}'")
        raise
