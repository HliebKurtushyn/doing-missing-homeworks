from extract import extract_csv, extract_api
from transform import double_column
from load import load_parquet


def main():
    df = extract_csv("input.csv")
    df = double_column(df, "Price")
    load_parquet(df, "output.parquet")

    # Приклад вилучення даних з API та перевірки валідності.
    api_data = extract_api(
        "https://jsonplaceholder.typicode.com/posts"
    )
    print(f"Отримано записів з API: {len(api_data)}")


if __name__ == "__main__":
    main()