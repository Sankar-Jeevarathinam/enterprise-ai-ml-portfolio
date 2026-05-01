from openai import OpenAI

client = OpenAI(api_key="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")

def generate_executive_summary(df, doc_type):

    review_text = df.to_string()

    prompt = f"""
    Based on the following AI clause compliance review results for a {doc_type},
    generate a concise executive governance summary including:

    - overall document compliance health
    - major recurring risks
    - severity observations
    - whether human legal/compliance review is recommended

    Review Data:
    {review_text[:5000]}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content