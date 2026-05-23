import pandas as pd

data = {
    'TransactionID': [501, 502, 503, 504, 505],
    'TransactionDate': [
        '2023-12-01',
        '31/12/2023',
        'December 15, 2023',
        '2023/12/20',
        '2023-13-01'
    ]
}

transactions_df = pd.DataFrame(data)

transactions_df['TransactionDate'] = pd.to_datetime(
    transactions_df['TransactionDate'],
    errors='coerce',
    dayfirst=True
)

transactions_df['Year'] = transactions_df['TransactionDate'].dt.year
transactions_df['Month'] = transactions_df['TransactionDate'].dt.month

print(transactions_df)