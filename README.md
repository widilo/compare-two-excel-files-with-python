# Compare two Excel files using Python

The compare_excel_files Python script is designed to streamline the process of analyzing and identifying changes in stock levels between two Excel files. The underlying mechanism involves several key steps:

1. **Importing Libraries**:

   ```python
   import pandas as pd
   ```

   This line imports the `pandas` library and gives it the alias `pd`. `pandas` is a powerful data manipulation and analysis library in Python.

2. **Defining the Function**:

   ```python
   def compare_excel_files(file1, file2, output_file):
   ```

   This line defines a function named `compare_excel_files` that takes three arguments: `file1`, `file2`, and `output_file`. These arguments represent the file paths for the two input Excel files and the output Excel file.

3. **Reading Excel Files**:

   ```python
   df1 = pd.read_excel(file1)
   df2 = pd.read_excel(file2)
   ```

   These lines use `pandas` to read the Excel files specified by `file1` and `file2` and store them as DataFrames (`df1` and `df2` respectively). A DataFrame is a tabular data structure similar to a spreadsheet.

4. **Merging DataFrames**:

   ```python
   merged = df1.merge(df2, on='SKU', how='outer', suffixes=('_old', '_new'))
   ```

   This line merges the two DataFrames (`df1` and `df2`) based on a common column, in this case, `'SKU'`. The `how='outer'` parameter means that it will perform an outer join, which includes all rows from both DataFrames.

   The `suffixes=('_old', '_new')` parameter adds suffixes to the column names to indicate which DataFrame they originated from.

5. **Identifying Changed Rows**:

   ```python
   changed_rows = merged[merged['STOCK_old'] != merged['STOCK_new']]
   ```

   This line creates a new DataFrame `changed_rows` containing only the rows where the 'STOCK_old' column is not equal to the 'STOCK_new' column. This means it will contain rows where the stock levels have changed.

6. **Saving Changes to Excel File**:

   ```python
   changed_rows.to_excel(output_file, index=False)
   ```

   This line saves the DataFrame `changed_rows` to an Excel file specified by `output_file`. The `index=False` parameter ensures that the row indices are not included in the output.

7. **Usage Example**:

   ```python
   compare_excel_files('file1.xlsx', 'file2.xlsx', 'changes.xlsx')
   ```

   This line calls the `compare_excel_files` function with the file paths `'file1.xlsx'` and `'file2.xlsx'` as input, and specifies `'changes.xlsx'` as the output file.

In summary, this script reads two Excel files, merges them based on the 'SKU' column, identifies rows with changes in the stock levels, and saves the changes to a new Excel file. The script provides a convenient way to compare two sets of stock data.

## Installation

To install and use this Python script along with its dependencies, you can follow these steps:

1. **Clone the GitHub repository**:

   You can clone the repository using Git. Open your terminal/command prompt and run:

   ```
   git clone https://github.com/widilo/compare-two-excel-files-with-python.git
   ```

2. **Install the dependencies**:

   Run the following command to install the required dependencies using `pip`:

   ```
   pip install -r requirements.txt
   ```

3. **Run the script**:

   To execute the script, simply run it using a Python interpreter:

   ```
   python compare_excel_files.py
   ```

Note: Make sure you have Python and Git installed on your system before following these steps.

## How to add additional columns

As an example, let's add a "Price" column to the script. We'll assume that the SKU values remain constant, while the STOCK and PRICE values may change:

```python
import pandas as pd

def compare_excel_files(file1, file2, output_file):
    # Read the Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Merge the data frames on the 'SKU' column
    merged = df1.merge(df2, on='SKU', how='outer', suffixes=('_old', '_new'))

    # Identify rows with changes in stock or price
    changed_rows = merged[(merged['STOCK_old'] != merged['STOCK_new']) | 
                          (merged['PRICE_old'] != merged['PRICE_new'])]

    # Save the changes to a new Excel file
    changed_rows.to_excel(output_file, index=False)

# Usage example
compare_excel_files('file1.xlsx', 'file2.xlsx', 'changes.xlsx')
```

In this modified script, we've added a new column called "PRICE". The script now identifies rows with changes in both STOCK and PRICE.
The script will now compare both stock levels and prices, identifying rows where either or both of these values have changed.

