import pandas as pd

def numeric_column_conversion(df):
    numeric_candidate = [
        "Quantity",
        "Price Per Unit",
        "Total Spent",
    ]

    for column in numeric_candidate:

        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )


def handle_missing_values(df):

    if df is None:
        print(f"❌ No Dataset Loaded.")
        return

    print("\n" + "=" * 50)
    print("              ZERO CLEANER")
    print("=" * 50)

    print("\n✅ Missing Values Detected")
    print("Please choose how ZERO should handle them:\n")

    print("[1] Remove Rows With Missing Values")
    print("    Recommended when dataset is large.\n")

    print("[2] Fill Text Columns With 'Unknown'")
    print("    Recommended for categorical columns.\n")

    print("[3] Fill Numeric Columns With Median")
    print("    Recommended for numerical analysis.\n")

    print("[4] Skip Cleaning")
    print("    Continue without modifying the data.\n")

    while True:
        choice = input(
            "\n Enter Choice (1-4): "
        )

        if choice in ["1", "2", "3", "4"]:
            break
        print(
            "\n❌ Invalid Choice. Please try again.\n"
        )
        print(
            "Please Enter any Number between 1-4: ",
        )

    if choice == "1":
        print(
            "\n✅ Option Selected"
        )
        print(
            "ZERO will attempt to remove incomplete rows"
        )
    elif choice == "2":
        print(
            "\n✅ Option Selected"
        )
        print(
            "ZERO will replace missing text values with 'Unknown'"
        )

        text_columns = df.select_dtypes(
            include = ["object"]
        ).columns

        for column in text_columns:
            df[column] = df[column].fillna("Unknown")

        print(
            df.isnull().sum()
        )

    elif choice == "3":
        print(
            "\n✅ Option Selected"
        )
        print(
            "ZERO will replace missing numeric Values with Median"
        )

        numeric_column_conversion(df)

        print("\nBEFORE CONVERSION")
        print(df.dtypes)

        # conversion code here

        print("\nAFTER CONVERSION")
        print(df.dtypes)

        numeric_columns = df.select_dtypes(
            include = ["number"]
        ).columns

        print("\nNumeric Columns Found:")

        print(numeric_columns)

        print(df[["Quantity",
                  "Price Per Unit",
                  "Total Spent"]].head(20))

        for column in numeric_columns:
            median_values = df(column).median()
            df[column] = df[column].fillna(
                median_values
            )
        print("\n✅ Cleaning Complete")

        print("\nUpdated Missing Vales Report")

        print(df.isnull().sum())

    elif choice == "4":
        print(
            "\n✅ Option Selected"
        )
        print(
            "You have Skipped the Operation"
        )
    else:
        print(
            f"Invalid Choice"
        )






from datat_loader import load_data

df = load_data("cafe_sales.csv")

handle_missing_values(df)

print("\n✅ Cleaning Completed")

print(
    "\nUpdated Missing Values Report"
)

print(f"Thank You for using Cleaner")