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
    print("\nCOLUMN TYPE REPORT")
    print("--------------------")

    for column in df.columns:

        print(
            f"{column} : {df[column].dtype}"
        )


from datat_loader import load_data

df = load_data("cafe_sales.csv")

data_summery(df)

column_type_report(df)