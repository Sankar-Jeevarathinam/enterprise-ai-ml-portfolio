import json
from openai import OpenAI

client = OpenAI(api_key="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")

def review_clause_with_llm(clause_text, doc_type):

    prompt = f"""
    You are a senior financial services compliance reviewer.

    Review the following {doc_type} clause and identify the single most critical compliance concern.

    Evaluate highest risk among:
    ambiguous wording,
    hidden fee exposure,
    legal liability imbalance,
    customer-unfriendly language,
    weak disclosure transparency,
    readability concerns.

    Clause:
    {clause_text}

    Return ONLY valid JSON in this exact schema:

    {{
      "Risk Category": "",
      "Severity": "",
      "Issue Found": "",
      "Explanation": "",
      "Recommended Safer Verbiage": "",
      "Compliance Score": 0
    }}

    Compliance Score must be integer 0 to 100.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0,
        response_format={"type": "json_object"}
    )

    return response.choices[0].message.content