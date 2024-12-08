import pandas as pd

# Read JSON file into a DataFrame
df = pd.read_json('data.json', lines=True)

# Display the DataFrame
print(df)
