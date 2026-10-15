import pandas as pd


def double_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found.")

    df = df.copy()
    df[f"{column}_doubled"] = df[column] * 2

    return df