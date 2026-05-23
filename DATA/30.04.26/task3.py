import pandas as pd

dates_df = pd.DataFrame({
    'EntryID': [701, 702, 703, 704, 705],
    'DateString': [
        '2024-02-30',
        '02/28/2024',
        '2024/03/15',
        'March 32, 2024',
        '2024-04-10'
    ]
})

dates_df['DateString'] = pd.to_datetime(
    dates_df['DateString'],
    errors='coerce'
)

print(dates_df)