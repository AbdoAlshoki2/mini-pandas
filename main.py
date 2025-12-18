from DataFrame import DataframeObject
def main():
    df = DataframeObject.read_csv()
    print(df.count_nulls())
    res = df.describe(file_name='stats_before_filling.csv')
    for key, value in res.items():
        print(f"{key}: {value}")

    print("\nFilling missing values...")
    df.fillna(num_strategy='mean', str_strategy='mode')
    print(df.count_nulls())
    res = df.describe(file_name='stats_after_filling.csv')
    for key, value in res.items():
        print(f"{key}: {value}")
    
    df.to_csv('filled_data.csv')

    print("\nReloading filled data from CSV...")
    df = DataframeObject.read_csv('filled_data.csv')
    print(df.count_nulls())


if __name__ == "__main__":
    main()