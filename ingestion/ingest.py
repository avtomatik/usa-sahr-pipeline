from core.paths import RAW_DATA
from core.warehouse import connect


def main():
    con = connect()

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


if __name__ == "__main__":
    main()
