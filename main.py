from DataFrame import DataframeObject
def main():
    # TODO: Read data


    # TODO: Fill missing values
    # Numeric columns → mean
    # Categorical columns → mode


    # TODO:Generate statistics file


    # TODO:Write cleaned data to CSV
    pass


if __name__ == "__main__":
    df = DataframeObject.read_csv()
    print(df.count_nulls())
