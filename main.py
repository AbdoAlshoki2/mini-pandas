from DataFrame import DataframeObject
from Stats import stats as st

def main():
    df = DataframeObject.read_csv()
    print(df.count_nulls())
    res = df.describe(file_name='stats_before_filling.csv')
    for key, value in res.items():
        print(f"{key}: {value}")
    
    print("="*40)


    print("\nFilling missing values...")
    df.fillna(num_strategy='mean', str_strategy='mode')
    print(df.count_nulls())
    res = df.describe(file_name='stats_after_filling.csv')

    print("="*40)

    for key, value in res.items():
        print(f"{key}: {value}")
    
    df.to_csv('filled_data.csv')

    print("="*40)

    print("\nReloading filled data from CSV...")
    df = DataframeObject.read_csv('filled_data.csv')
    print(df.count_nulls())

    print("="*40)

    print(st.get_stat(df.get_data(), df.get_dtype(), st.get_col_mean))

    print("="*40)

    print(df)

if __name__ == "__main__":
    main()