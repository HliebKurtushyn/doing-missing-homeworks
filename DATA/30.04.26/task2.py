import pandas as pd

timestamps_df = pd.DataFrame({
    'TimestampID': [601, 602, 603, 604],
    'UnixTimestamp': [1704067200, 1704153600, 1704240000, 1704326400]
})

timestamps_df['Datetime'] = pd.to_datetime(
    timestamps_df['UnixTimestamp'],
    unit='s'
)

timestamps_df['Year'] = timestamps_df['Datetime'].dt.year
timestamps_df['Month'] = timestamps_df['Datetime'].dt.month
timestamps_df['Day'] = timestamps_df['Datetime'].dt.day
timestamps_df['Hour'] = timestamps_df['Datetime'].dt.hour

print(timestamps_df)