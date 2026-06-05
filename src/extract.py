import duckdb

from .core.paths import RAW_DATA


def ingest_raw(con: duckdb.DuckDBPyConnection) -> None:
    """
    Load raw JSON.GZ dataset into DuckDB.

    Creates:
        raw.sahr
    """

    con.execute(
        """
        CREATE SCHEMA IF NOT EXISTS raw
        """
    )

    con.execute(
        """
        CREATE OR REPLACE TABLE raw.sahr AS
        SELECT *
        FROM read_json_auto(?)
        """,
        [str(RAW_DATA)],
    )
