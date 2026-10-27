def handle_missing_values(df):

    print(
        "\nMISSING VALUE HANDLER"
    )
    print(
        "Choose how to handle missing values"
    )
    print(
        "1. Remove Rows"
    )
    print(
        "2. Fill text columns with 'Unknown'"
    )
    print(
        "3. Fill Numeric columns with Median"
    )
    print(
        "4. Skip"
    )

    choice = input(
        "Enter Choice (1-4): "
    )

    if choice == "1":
        print(
            f"Removing Rows..."
        )
    elif choice == "2":
        print(
            f"Fill text columns with Selected"
        )
    elif choice == "3":
        print(
            f"Fill Numeric columns with Selected"
        )
    elif choice == "4":
        print(
            f"Skipping Cleaning"
        )
    else:
        print(
            f"Invalid Choice"
        )

from datat_loader import load_data

df = load_data("cafe-sales.csv")

handle_missing_values(df)