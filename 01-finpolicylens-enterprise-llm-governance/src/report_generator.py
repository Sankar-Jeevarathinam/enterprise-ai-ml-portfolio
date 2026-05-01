import pandas as pd

def generate_summary_report(results):

    df = pd.DataFrame(results)

    avg_score = round(df["Compliance Score"].mean(), 2)
    flagged = len(df[df["Compliance Score"] < 75])

    summary = {
        "Clauses Reviewed": len(df),
        "Flagged Clauses": flagged,
        "Average Compliance Score": avg_score
    }

    return df, summary