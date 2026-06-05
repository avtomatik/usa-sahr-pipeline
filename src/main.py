#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:26:17 2023

@author: green-machine
"""


from .extract import ingest_raw
from .load import connect
from .transform import compute_inflation_rates


def main() -> None:

    con = connect()

    ingest_raw(con)

    df = con.execute(
        """
        SELECT
            series_name,
            year,
            conversion_factor
        FROM raw.sahr
        ORDER BY
            year,
            series_name
        """
    ).df()

    (
        compute_inflation_rates(df).plot(
            grid=True,
            title="USA SAHR Inflation-Adjusted Rates",
        )
    )


if __name__ == "__main__":
    main()
