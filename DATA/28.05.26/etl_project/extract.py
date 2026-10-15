import json
import requests
import pandas as pd


def extract_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def extract_api(url: str, json_path: str = "intermediate.json") -> list:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    if not isinstance(data, list):
        raise ValueError("API response must be a list.")

    required_fields = {"id", "title"}

    for item in data:
        if not isinstance(item, dict) or not required_fields.issubset(item):
            raise ValueError("Invalid data: required fields are missing.")

    return data