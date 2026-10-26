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

def column_type_report(df):
    print(f"COLUMN TYPE REPORT")
    if df.dtypes == "object":
        print(f"Transection ID: {df.columns}")
        print(f"Items: {df.dtypes}")
        print(f"Location: {df.columns}")
    elif df.dtypes == "Integer":
        print(f"Quantity: {df.columns}")
    elif df.dtypes == "Float":
        print(f"Price: {df.columns}")
        print(f"TotalSpent: {df.columns}")
    else:
        print(f"Type: {df.dtypes}")

    return df


from datat_loader import load_data

df = load_data("cafe_sales.csv")

data_summery(df)