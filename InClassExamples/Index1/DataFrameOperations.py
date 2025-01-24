import pandas as pd

# Create a sample DataFrame

df = pd.DataFrame({

'A': [3, 2, 1, 4],

'B': [5, 6, 5, 8],

'C': ['foo', 'bar', 'baz', 'qux']

})

# Initial DataFrame

print("Initial DataFrame:")

print(df)

print()

# Sort the DataFrame by column 'A'

df_sorted = df.sort_values(by='A')

print("# After sorting by column 'A':")

print(df_sorted)

print()

# Sort the DataFrame by columns 'A' and 'B'

df_sorted_multiple = df.sort_values(by=['A', 'B'])

print("# After sorting by columns 'A' and 'B':")

print(df_sorted_multiple)

# Sort the DataFrame by column 'A' in descending order

df_sorted_desc = df.sort_values(by='A', ascending=False)

print("# After sorting by column 'A' in descending order:")

print(df_sorted_desc)

# Create a sample DataFrame with a custom index

df_with_index = pd.DataFrame({

'A': [3, 2, 1, 4],

'B': [5, 6, 7, 8],

'C': ['foo', 'bar', 'baz', 'qux']

}, index=['d', 'a', 'b', 'c'])

# Sort the DataFrame by its index

df_sorted_index = df_with_index.sort_index()

print("# After sorting by index:")

print(df_sorted_index)