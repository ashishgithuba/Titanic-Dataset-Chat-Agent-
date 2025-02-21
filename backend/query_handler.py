import pandas as pd

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

def process_query(query: str):
    query = query.lower()

    if "percentage of passengers were male" in query:
        male_count = df[df["Sex"] == "male"].shape[0]
        total_count = df.shape[0]
        percentage = (male_count / total_count) * 100
        return f"{percentage:.2f}% of passengers were male."

    elif "histogram of passenger ages" in query:
        return "histogram"

    elif "average ticket fare" in query:
        avg_fare = df["Fare"].mean()
        return f"The average ticket fare was ${avg_fare:.2f}."

    elif "how many passengers embarked" in query:
        embark_counts = df["Embarked"].value_counts().to_dict()
        return embark_counts

    return "Sorry, I couldn't understand that query."
