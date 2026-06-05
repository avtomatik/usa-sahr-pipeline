import duckdb

from .core.paths import WAREHOUSE


def connect() -> duckdb.DuckDBPyConnection:
    """Create warehouse connection."""
    return duckdb.connect(str(WAREHOUSE))
