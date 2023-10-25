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
