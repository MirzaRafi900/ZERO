import pandas as pd


def data_summery(df):

    rows = df.shape[0]
    columns = df.shape[1]
    missing_values = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()


    print(f"DATASET SUMMERY")
    print(f"---------------")
    print(f"Rows: {rows}")
    print(f"Columns: {columns}")
    print(f"Missing Values: {missing_values}")
    print(f"Duplicates: {duplicates}")


from datat_loader import load_dataset

df = load_dataset("cafe_sales.csv")

data_summery(df)