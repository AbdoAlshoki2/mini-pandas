from FileHandler import file_handler as fh
from Stats import stats as st
class DataframeObject:
    def __init__(self, data:dict, dtype:dict):
        """
        Initialize the Dataframe with data and data types.
        Args:
            data (dict): Dictionary where keys are column names and values are lists of column values.
            dtype (dict): Dictionary where keys are column names and values are data types ('int', 'float', 'string').
        """
        self.data = data
        self.dtype = dtype
        print("Dataframe initialized.")
    
    @classmethod
    def read_csv(cls, file_name='titanic.csv', dtype_file='titanic_dtype.csv'):
        """
        Class method to read a CSV file and its data types, returning a Dataframe instance.
        Args:
            file_name (str): Name of the CSV data file in the 'data' directory.
            dtype_file (str): Name of the CSV file in the 'data' directory containing column names and types.
        Returns:
            Dataframe: An instance of the Dataframe class with loaded data and data types.
        """
        dtypes = fh.read_dtype(file_name=dtype_file)
        data = fh.read_csv_file(file_name=file_name, dtypes=dtypes)
        return cls(data, dtypes)
    
    def count_nulls(self):
        """
        Count the number of null (None) values in each column of the Dataframe.
        Returns:
            dict: A dictionary where keys are column names and values are counts of null values.
        """
        null_counts = {}
        for col_name, values in self.data.items():
            null_counts[col_name] = sum(1 for v in values if v is None)
        return null_counts

    
    def fillna(self, num_strategy='mean', str_strategy='mode'):
        """
        Fill null (None) values in the Dataframe using specified strategies for numerical and string columns.
        Args:
            num_strategy (str): Strategy for numerical columns ('mean', 'median', 'mode').
            str_strategy (str): Strategy for string columns ('mode').
        """
        for col_name, values in self.data.items():
            if self.dtype[col_name] in ['int', 'float']:
                if num_strategy == 'mean':
                    fill_value = st.get_col_mean(values)
                elif num_strategy == 'median':
                    fill_value = st.get_col_median(values)
                elif num_strategy == 'mode':
                    fill_value = st.get_col_mode(values)
                elif num_strategy == 'max':
                    fill_value = st.get_col_max(values)
                elif num_strategy == 'min':
                    fill_value = st.get_col_min(values)
                else:
                    raise ValueError(f"Unknown numerical strategy: {num_strategy}")
                
                self.data[col_name] = [v if v is not None else fill_value for v in values]

            else:
                if str_strategy == 'mode':
                    fill_value = st.get_col_mode(values)
                else:
                    raise ValueError(f"Unknown string strategy: {str_strategy}")
                
                self.data[col_name] = [v if v is not None else fill_value for v in values]
               

    def describe(self, file_name='statistics_output.csv'):
        """
        Generate basic statistics for numeric columns in the Dataframe.
        Returns:
            dict: A dictionary where keys are column names and values are dictionaries of statistics (mean, median, std).
        """
        result = {}
        result['columns'] = list(self.data.keys())
        nulls = self.count_nulls()
        result['null_counts'] = [nulls[col] for col in result['columns']]

        mean_stats = st.get_stat(self.data, self.dtype, st.get_col_mean)
        result['mean'] = [mean_stats[col] if col in mean_stats.keys() else None for col in result['columns'] ]

        median_stats = st.get_stat(self.data, self.dtype, st.get_col_median)
        result['median'] = [median_stats[col] if col in median_stats.keys() else None for col in result['columns']]

        max_stats = st.get_stat(self.data, self.dtype, st.get_col_max)
        result['max'] = [max_stats[col] if col in max_stats.keys() else None for col in result['columns']]

        min_stats = st.get_stat(self.data, self.dtype, st.get_col_min)
        result['min'] = [min_stats[col] if col in min_stats.keys() else None for col in result['columns']]

        result['mode'] = [st.get_col_mode(self.data[col]) for col in result['columns']]

        fh.write_file(file_name, result)
        print(f"Statistics file generated: {file_name}")
        return result


    def to_csv(self, file_name):
        """
        Write the Dataframe data to a CSV file.
        Args:
            file_name (str): Name of the output CSV file in the 'data' directory.
        Returns:
            None
        """
        fh.write_file(file_name, self.data)
        print(f"Data written to {file_name}.")

    
    def __str__(self):
        return f"Dataframe with columns: {list(self.data.keys())}"
    
    def __repr__(self):
        return self.__str__()

    def get_data(self):
        """
        Get the underlying data dictionary of the Dataframe.
        Returns:
            dict: The data dictionary where keys are column names and values are lists of column values.
        """
        return self.data
    
    def get_dtype(self):
        """
        Get the data types dictionary of the Dataframe.
        Returns:
            dict: The data types dictionary where keys are column names and values are data types ('int', 'float', 'string').
        """
        return self.dtype
        

