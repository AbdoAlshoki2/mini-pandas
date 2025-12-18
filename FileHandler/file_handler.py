import csv
import os

def read_csv_file(file_name = 'titanic.csv', dtypes:dict = None):
    """
    Read a CSV file and convert each column to the specified data type.

    Args:
        file_path (str): Path to the CSV data file.
        dtypes (dict): Dictionary mapping column names to data types ('int', 'float', 'string').

    Returns:
        dict: A dictionary where keys are column names and values are lists of column values.
              Missing values (empty strings) are replaced with None.
    
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(project_root, 'data', file_name)

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        tmp = list(reader)
    data = {key: [] for key in tmp[0].keys()}
    data = {
        key: [
            None if row[key] == '' else
            int(row[key]) if dtypes and dtypes.get(key) == 'int' else
            float(row[key]) if dtypes and dtypes.get(key) == 'float' else
            row[key]
            for row in tmp
        ]
        for key in data.keys()
    }
    return data

def read_dtype(file_name = 'titanic_dtype.csv'):
    
    """
    Read a CSV file containing column names and their data types.

    Args:
        file_path (str): Path to the CSV file containing column names and types.

    Returns:
        dict: A dictionary where keys are column names and values are data types ('int', 'float', 'string').
    """

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(project_root, 'data', file_name)

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {row['column']: row['dtype'] for row in reader}

    return data
            
def write_file(file_name, data:dict):
    """
    Write a data dictionary to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (dict): Dictionary where keys are column names and values are lists of column values.

    Returns:
        None
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(project_root, 'data', file_name)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data.keys())
        rows = zip(*data.values())
        writer.writerows(rows)
