from openai import OpenAI

client = OpenAI(api_key="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")

def classify_document(document_text):

    prompt = f"""
    Classify the following uploaded business/financial document into one of these categories only:

    - Lending Agreement
    - Insurance Policy
    - Vendor Contract
    - Fee Disclosure
    - Internal Compliance Policy
    - General Financial Document

    Document:
    {document_text[:2000]}

    Return only the category name.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()