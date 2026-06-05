import pandas as pd


def extract_series(df: pd.DataFrame, series_name: str) -> pd.DataFrame:
    """
    Extract one conversion-factor series.
    """

    series = df.loc[
        df["series_name"] == series_name,
        "conversion_factor",
    ]

    return series.rename(series_name).to_frame()


def compute_inflation_rates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute inflation rates from conversion factors.
    """

    df = df[
        [
            "series_name",
            "year",
            "conversion_factor",
        ]
    ].copy()

    df = df.set_index("year")

    num_series_to_use = 14

    series_ids = df["series_name"].unique()[:num_series_to_use]

    combined = pd.concat(
        [extract_series(df, sid).rdiv(1) for sid in series_ids],
        axis=1,
        join="outer",
    )

    return combined.pct_change().mul(-1)
