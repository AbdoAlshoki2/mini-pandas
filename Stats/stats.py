from functools import reduce

def get_col_max(col:list):
    """
    Compute the maximum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The maximum value in the column (numeric type).
    """

    max_number = reduce(lambda x , y : x if (x > y) else y, [v for v in col if v is not None])
    return max_number
    

def get_col_min(col:list):
    """
    Compute the minimum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The minimum value in the column (numeric type).
    """
    min_number = reduce(lambda x , y : x if (x < y) else y, [v for v in col if v is not None])
    return min_number

def get_col_mean(col:list):
    """
    Compute the mean (average) value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The mean value of the column (float).
    """
    clean_col = [v for v in col if v is not None]
    cur_sum = 0
    for v in clean_col:
        cur_sum += v
    mean_number = cur_sum / len(clean_col) if len(clean_col) > 0 else 0
    return mean_number  

def get_col_median(col:list):
    """
    Compute the median value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The median value of the column (numeric type).
    """
    clean_col = [v for v in col if v is not None]
    clean_col.sort()
    n = len(clean_col)
    if n == 0:
        return None
    if n % 2 == 1:
        median_number = clean_col[n // 2]
    else:
        median_number = (clean_col[n // 2 - 1] + clean_col[n // 2]) / 2
    return median_number

def get_col_mode(col:list):
    """
    Compute the mode (most frequent value) of a column.

    Args:
        col (list): A list of values. `None` values are ignored.

    Returns:
        The mode value of the column. If multiple values have the same
        frequency, the first encountered is returned.
    """
    clean_col = [v for v in col if v is not None]
    clean_col.sort()
    cnt = 1
    mx_cnt = 1
    mode = clean_col[0] if len(clean_col) > 0 else None
    for i in range(1, len(clean_col)):
        if clean_col[i] == clean_col[i - 1]:
            cnt += 1
        else:
            cnt = 1

        if cnt > mx_cnt:
            mx_cnt = cnt
            mode = clean_col[i]
    
    return mode
    

def get_stat(data:dict, dtypes:dict, function):
    """
    Apply a statistical function to all numerical columns in a dataset.

    Args:
        data (dict): Dictionary where keys are column names and values are lists of column values.
        dtypes (dict): Dictionary where keys are column names and values are data types ('int', 'float', 'string').
        function (function): A function to apply to each numerical column (e.g., get_col_max, get_col_mean).

    Returns:
        dict: A dictionary where keys are column names and values are the result
        of applying the function to that column. Only numerical columns are processed.
    """
    result = {}
    for col_name, col_values in data.items():
        if dtypes[col_name] in ['int', 'float']:
            result[col_name] = function(col_values)
    return result





