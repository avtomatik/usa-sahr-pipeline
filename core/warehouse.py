import duckdb

from core.paths import WAREHOUSE


def connect() -> duckdb.DuckDBPyConnection:
    return duckdb.connect(str(WAREHOUSE))
