import pandas as pd

students_data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Subject1": [85, 78, 92, 60],
    "Subject2": [88, 74, 95, 65],
    "Subject3": [90, 80, 85, 70]
}

df = pd.DataFrame(students_data)

df["Total"] = df[["Subject1", "Subject2", "Subject3"]].sum(axis=1)
df["Average"] = df["Total"] / 3

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

class_avg = df["Average"].mean()
topper = df.loc[df["Average"].idxmax()]

print("--- Student Summary ---")
print(df)

print(f"\nClass Average: {class_avg:.2f}")
print(f"Topper: {topper['Name']} with Average: {topper['Average']:.2f} and Grade: {topper['Grade']}")
