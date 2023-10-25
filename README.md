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
    changed_rows = merged[merged['BESTAND_old'] != merged['BESTAND_new']]

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
5. It identifies rows where the 'BESTAND' values have changed.
6. It saves the changed rows to a new Excel file using `to_excel`.

Remember to replace `'file1.xlsx'`, `'file2.xlsx'`, and `'changes.xlsx'` with the actual paths of your input and output files.

## How to add a requirements.txt file

To generate a `requirements.txt` file for the Python script, you can list the necessary libraries along with their versions. For your specific script, you'll need the `pandas` library.

Here's what your `requirements.txt` file should look like:

```makefile
pandas==1.3.3
```

You can create this file manually and save it in the same directory as your Python script. Then, when someone wants to use your script, they can run `pip install -r requirements.txt` to install the required libraries.

For comparing Excel files and saving changes, the `pandas` library is the primary one you'll need. However, if your script has additional functionality, you might need other libraries.

If you're using any additional libraries, make sure to include them in the `requirements.txt` file along with their versions. For example, if your script also uses `openpyxl` for Excel file handling, you would add it to the `requirements.txt` file like this:

```makefile
pandas==1.3.3
openpyxl==3.0.9
```

Remember, the libraries you include in `requirements.txt`  should be those that are not part of the standard library in Python. If  your script relies on standard libraries, there's no need to include  them in `requirements.txt`.

## Installation Guide

### Step 1: Clone or Download the Repository

You can either clone the repository using Git or download it as a zip file and extract the contents.

```bash
git clone https://github.com/your_username/your_repository.git
```

### Step 2: Navigate to the Directory

```bash
cd your_repository
```

### Step 3: Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv env
```

### Step 4: Activate the Virtual Environment (Optional)

On Windows:

```bash
.\env\Scripts\activate
```

On macOS and Linux:

```bash
source env/bin/activate
```

### Step 5: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Usage

### Running the Script

```bash
python compare_excel.py file1.xlsx file2.xlsx changes.xlsx
```

Replace `file1.xlsx`, `file2.xlsx`, and `changes.xlsx` with the actual paths.

## Documentation

### Overview

The `compare_excel.py` script is designed to compare two Excel files and save the changes in a new file. It specifically looks at the 'BESTAND' column for changes while keeping the 'SKU' column constant.

### Usage

```
python compare_excel.py <file1> <file2> <output_file>
```

- `<file1>`: Path to the first input Excel file.
- `<file2>`: Path to the second input Excel file.
- `<output_file>`: Path where the changes will be saved.

### Example

```bash
python compare_excel.py file1.xlsx file2.xlsx changes.xlsx
```

### Requirements

The script relies on the following library:

- `pandas==1.3.3`

### Notes

- The script assumes that the Excel files are well-formed and contain the columns 'SKU' and 'BESTAND'.
- The 'SKU' column is used as the key to identify and compare rows between the two files.
- The changes are saved in a new Excel file specified by `<output_file>`.

------

Remember to customize the file names, paths, and any additional information based on your actual script. This serves as a basic template that you can expand upon depending on the complexity and specific functionality of your script.

## Add more columns?

To add more columns for comparison, you'll need to modify the script to handle the additional columns. You can follow these steps:

**1. Update Function Parameters**:

Modify the function `compare_excel_files` to accept a list of column names that you want to compare. For example, if you want to compare both 'BESTAND' and 'PRICE' columns, the function signature would look like this:

```python
def compare_excel_files(file1, file2, output_file, columns_to_compare):
    # ...
```

**2. Update Data Reading and Merging**:

When reading the Excel files, ensure that you include the additional columns you want to compare. For example, if you want to include 'PRICE', you would modify the reading part like this:

```python
df1 = pd.read_excel(file1, usecols=['SKU', 'BESTAND', 'PRICE'])
df2 = pd.read_excel(file2, usecols=['SKU', 'BESTAND', 'PRICE'])
```

**3. Update Merge Process**:

When merging the data frames, you will need to specify the additional columns you want to compare in the `suffixes` parameter. For example, if you're comparing 'BESTAND' and 'PRICE', you might use:

```python
merged = df1.merge(df2, on='SKU', how='outer', suffixes=('_old', '_new'))
```

**4. Identify Rows with Changes**:

Modify the line where you identify rows with changes to include the additional columns:

```python
changed_rows = merged[(merged['BESTAND_old'] != merged['BESTAND_new']) | (merged['PRICE_old'] != merged['PRICE_new'])]
```

**5. Update Output File**:

When saving the changes, you'll need to include the additional columns:

```python
changed_rows.to_excel(output_file, index=False, columns=['SKU', 'BESTAND_old', 'BESTAND_new', 'PRICE_old', 'PRICE_new'])
```

**6. Usage Example**:

When calling the function, make sure to provide the list of columns to compare:

```python
compare_excel_files('file1.xlsx', 'file2.xlsx', 'changes.xlsx', ['BESTAND', 'PRICE'])
```

This example assumes you want to add the 'PRICE' column for comparison. You can repeat the process for any additional columns you want to include. Remember to update the function, data reading, merging, change identification, and output file saving steps accordingly.

Please note that the function and code might need further adjustments depending on the specifics of your data and what you want to achieve. Always test thoroughly after making significant changes.

Here's the modified script that can compare multiple columns:

```python
import pandas as pd

def compare_excel_files(file1, file2, output_file, columns_to_compare):
    # Read the Excel files with specified columns
    df1 = pd.read_excel(file1, usecols=['SKU'] + columns_to_compare)
    df2 = pd.read_excel(file2, usecols=['SKU'] + columns_to_compare)

    # Merge the data frames on the 'SKU' column
    merged = df1.merge(df2, on='SKU', how='outer', suffixes=('_old', '_new'))

    # Identify rows with changes
    condition = any(merged[f'{col}_old'] != merged[f'{col}_new'] for col in columns_to_compare)
    changed_rows = merged[condition]

    # Save the changes to a new Excel file with specified columns
    columns_to_save = ['SKU'] + [f'{col}_old' for col in columns_to_compare] + [f'{col}_new' for col in columns_to_compare]
    changed_rows.to_excel(output_file, index=False, columns=columns_to_save)

# Usage example with 'BESTAND' and 'PRICE' columns
compare_excel_files('file1.xlsx', 'file2.xlsx', 'changes.xlsx', ['BESTAND', 'PRICE'])
```

In this script, we've added a `columns_to_compare` parameter to the `compare_excel_files` function. This parameter should be a list of column names you want to compare.

The script will now compare the 'SKU', 'BESTAND', and 'PRICE' columns. You can modify the list of columns in the `compare_excel_files` function call to include any additional columns you want to compare.

Please make sure to replace `'file1.xlsx'`, `'file2.xlsx'`, and `'changes.xlsx'` with your actual file paths.



## Contributing Guidelines

We welcome contributions from the community! If you'd like to contribute to this project, please follow these guidelines:

### 1. Fork the Repository

Click the "Fork" button at the top right corner of this page to create your own copy of the repository.

### 2. Clone Your Fork

Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/your_repository.git
```

### 3. Create a Branch

Create a new branch for your work:

```bash
cd your_repository
git checkout -b feature_branch
```

### 4. Make Changes

Make your desired changes to the code.

### 5. Test Your Changes

Before submitting a pull request, make sure your changes work as expected. Test thoroughly to avoid introducing bugs.

### 6. Commit Your Changes

Commit your changes with a descriptive commit message:

```bash
git add .
git commit -m "Description of your changes"
```

### 7. Push Your Changes

Push the changes to your fork:

```bash
git push origin feature_branch
```

### 8. Create a Pull Request

Go to the original repository and click on the "Pull Requests" tab. Click the "New Pull Request" button, select your branch, and click "Create Pull Request". Provide a descriptive title and details about your changes.

### 9. Review and Discuss

We will review your pull request and may ask for clarifications or suggest improvements. Be prepared to engage in a discussion about your changes.

### 10. Merge and Celebrate!

Once your pull request is approved, it will be merged into the main branch. Congratulations on your contribution!

### Code Style and Guidelines

Please adhere to the following guidelines:

- Follow the existing code style and conventions.
- Write clear and concise code with meaningful variable names and comments where necessary.
- Keep functions and methods modular and well-documented.

### Bug Reports and Feature Requests

If you find a bug or have a feature request, please open an issue on the GitHub repository.

### License

By contributing to this project, you agree that your contributions will be licensed under the [LICENSE](https://chat.openai.com/c/link_to_license) file.

 <p xmlns:cc="http://creativecommons.org/ns#"  xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title"  rel="cc:attributionURL"  href="https://teufelswerk.net/repository">Compare two Excel files  using Python</a> by <a rel="cc:attributionURL dct:creator"  property="cc:attributionName"  href="https://teufelswerk.net">teufelswrk</a> is licensed under  <a  href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1"  target="_blank" rel="license noopener noreferrer"  style="display:inline-block;">CC BY-NC-SA 4.0<img  style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"   src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img   style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"   src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img   style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"   src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img   style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"   src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>  



------

