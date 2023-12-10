import pandas as PD

# Read the file into a DataFrame
df = pd.read_csv('test3.csv')

# Specify columns for duplicate check
columns_to_check = ['column1', 'column2']

# Check for duplicates based on selected columns
duplicates = df.duplicated(subset=columns_to_check, keep=False)

# Filter the DataFrame to show duplicate rows
duplicate_rows = df[duplicates]

# Display duplicate rows (you can customize this part based on your needs)
print("Duplicate Rows:")
print(duplicate_rows)

# Optionally, you can fail the workflow if duplicates are found
if not duplicate_rows.empty:
    print("Error: Duplicates found.")
    exit(1)
