import pandas as pd

# Create a Series

data_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd',
'e'])

print("Series:")

print(data_series)

print()

# Create a DataFrame

data_frame = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]},
index=['a', 'b', 'c'])

print("DataFrame:")

print(data_frame)

print()

# Accessing elements in Series

print("Access element in Series (index 'a'):")

print(data_series['a'])

print()

# Accessing elements in DataFrame

print("Access element in DataFrame (row 'a', column 'col1'):")

print(data_frame.at['a', 'col1'])

print()

# Accessing rows in DataFrame

print("Access row in DataFrame (row 'a'):")

print(data_frame.loc['a'])

print()

# Accessing columns in DataFrame

print("Access column in DataFrame (column 'col1'):")

print(data_frame['col1'])

print()

# Mathematical operations in Series

print("Series after adding 5 to each element:")

print(data_series + 5)

print()

# Mathematical operations in DataFrame

print("DataFrame after adding 10 to each element:")

print(data_frame + 10)

print()

# Aggregation in Series

print("Sum of elements in Series:")

print(data_series.sum())

print()

# Aggregation in DataFrame

print("Sum of elements in DataFrame:")

print(data_frame.sum())

print()

# Handling missing data in Series

data_series_with_nan = pd.Series([1, 2, None, 4, 5], index=['a', 'b',
'c', 'd', 'e'])

print("Series with missing data:")

print(data_series_with_nan)

print("Filled missing data in Series:")

print(data_series_with_nan.fillna(0))

print()

# Handling missing data in DataFrame

data_frame_with_nan = pd.DataFrame({'col1': [1, None, 3], 'col2': [4,
5, None]}, index=['a', 'b', 'c'])

print("DataFrame with missing data:")

print(data_frame_with_nan)

print("Filled missing data in DataFrame:")

print(data_frame_with_nan.fillna(0))

print()

# Plotting Series and DataFrame

import matplotlib.pyplot as plt

# Plot Series

data_series.plot(kind='bar', title='Series')

plt.show()

# Plot DataFrame

data_frame.plot(kind='bar', title='DataFrame')

plt.show()