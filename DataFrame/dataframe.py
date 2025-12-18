from FileHandler import file_handler as fh

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

    
    #TODO: define describe()


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
        

