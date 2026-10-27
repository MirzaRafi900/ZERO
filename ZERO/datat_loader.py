import pandas as pd


def load_data(file_path):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlxx"):
            df = pd.read_excel(file_path)
        else:
            return None

        return df


    except Exception as e:
        print(
            f"Error: {e}"
        )

        return None

if __name__ == "__main__":
    df = load_data("cafe_sales.csv")

    if df is not None:
        print(df.head(10))