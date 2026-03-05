import pandas as pd


def main():

    #sample dataset
    data = {
        "Name": ["Ram", "Nitin", "Arun", "Mina", "Nita", "Jacob"],
        "Score": [95, 92, 78, 88, 67, 90],
        "Passed": [True, True, False, True, False, True],
        "Category": ["A", "A", "B", "B", "A", "A"]
    }

    df = pd.DataFrame(data)

    print("\nOriginal Dataset:")
    print(df)

    #Select a single column
    print("\nSingle Column (Score):")
    score_column = df["Score"]
    print(score_column)

    #Select multiple columns
    print("\nMultiple Columns (Name, Score):")
    name_score_df = df[["Name", "Score"]]
    print(name_score_df)

    print("\nFirst three rows using iloc:")
    print(df.iloc[:3])

    df_indexed = df.set_index("Name")

    print("\nUsing loc to access row for Ram:")
    print(df_indexed.loc["Ram"])

    #Filter rows where Score > 85
    print("\nStudents with Score > 85:")
    high_score = df[df["Score"] > 85]
    print(high_score)

    #Filter rows where Score > 85 AND Passed = True
    print("\nStudents with Score > 85 AND Passed = True:")
    filtered = df[(df["Score"] > 85) & (df["Passed"] == True)]
    print(filtered)

    #filtered result by Score
    print("\nHigh-performing students sorted by Score:")
    ranked_students = filtered.sort_values(by="Score", ascending=False)
    print(ranked_students[["Name", "Score"]])


if __name__ == "__main__":
    main()