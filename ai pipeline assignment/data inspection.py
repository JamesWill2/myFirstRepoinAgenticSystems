import pandas as pd


def main():
    # sample dataset
    sample_data = {
        "Name": ["Anurag", "Kartik", "Ana", "David", "Anshul", "Ram"],
        "Age": [25, 23, 27, 31, 16, 34],
        "Score": [85, 78, 10, 88, 76, 5],
        "Label": ["Pass", "Pass", "Fail", "Pass", "Pass", "Fail"]
    }

    df = pd.DataFrame(sample_data)

    # Save as CSV
    df.to_csv("sample_dataset.csv", index=False)

    # Load dataset
    dataset = pd.read_csv("sample_dataset.csv")

    print("\n First 5 Rows ")
    print(dataset.head())

    print("\n Last 5 Rows ")
    print(dataset.tail())

    print("\n Dataset Info ")
    print(dataset.info())

    print("\n Summary Statistics ")
    print(dataset.describe())

    # Select single column
    print("\nSingle Column: Score ")
    score_column = dataset["Score"]
    print(score_column)

    # Select multiple columns
    print("\nMultiple Columns: Name and Score ")
    selected_columns = dataset[["Name", "Score"]]
    print(selected_columns)

    # Filter rows
    print("\nFiltered Rows (Score > 80)")
    filtered_rows = dataset[dataset["Score"] > 80]
    print(filtered_rows)


if __name__ == "__main__":
    main()