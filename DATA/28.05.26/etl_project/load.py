import pandas as pd
from sqlalchemy import create_engine


def load_parquet(df: pd.DataFrame, path: str = "output.parquet") -> None:
    df.to_parquet(path, index=False)


def load_database(
    df: pd.DataFrame,
    connection_string: str,
    table_name: str,
) -> None:
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    engine.dispose()