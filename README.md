# Compare two Excel files using Python

To achieve this, you can use the `pandas` library in Python. If you haven't already installed it, you can do so with `pip install pandas`. Here's a Python script that compares two Excel files based on the "SKU" column and saves the changes in a new file:

```python
import pandas as pd

def compare_excel_files(file1, file2, output_file):
    # Read the Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Merge the data frames on the 'SKU' column
    merged = df1.merge(df2, on='SKU', how='outer', suffixes=('_old', '_new'))

    # Identify rows with changes
    changed_rows = merged[merged['STOCK_old'] != merged['STOCK_new']]

    # Save the changes to a new Excel file
    changed_rows.to_excel(output_file, index=False)

# Usage example
compare_excel_files('file1.xlsx', 'file2.xlsx', 'changes.xlsx')

```

Here's what this script does:

1. It imports the `pandas` library.
2. The `compare_excel_files` function takes three arguments: `file1` and `file2` are the paths to the input Excel files, and `output_file` is the path where you want to save the changes.
3. It reads the Excel files using `pd.read_excel`.
4. It merges the data frames based on the 'SKU' column.
5. It identifies rows where the 'STOCK' values have changed.
6. It saves the changed rows to a new Excel file using `to_excel`.

Remember to replace `'file1.xlsx'`, `'file2.xlsx'`, and `'changes.xlsx'` with the actual paths of your input and output files.


