from core.warehouse import connect
from transform.logic import compute_inflation_rates


def main() -> None:

    con = connect()

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
            title="USA Sahr Inflation-Adjusted Rates",
        )
    )


if __name__ == "__main__":
    main()
