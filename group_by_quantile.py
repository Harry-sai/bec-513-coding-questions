import sys
import pandas as pd

# Step 1: Read the quantile count (Q1) from command-line arguments.
Q1 = int(sys.argv[1])

# Step 2: Read data from standard input into a pandas Series.
data = pd.read_csv(sys.stdin, names=['values']).squeeze('columns')

# Step 3: Divide the data into quantiles using pandas qcut.
pd.qcut(data.values, Q1)

# Step 4: Convert data back to a DataFrame.
data = pd.DataFrame(data)

# Step 5: Add a 'quantile' column with labels for each quantile (e.g., q1, q2...).
data['quantile'] = pd.qcut(data['values'], Q1, labels=[f'q{i+1}' for i in range(Q1)])

# Step 6: Add a 'range' column showing the value ranges for each quantile.
data['range'] = pd.qcut(data['values'], Q1)

# Step 7: Print the DataFrame with the values, quantile labels, and ranges.
print(data)

