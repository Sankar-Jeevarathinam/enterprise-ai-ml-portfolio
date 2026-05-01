from openai import OpenAI

moderation_client = OpenAI(api_key="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")

def input_moderation(document_text):

    try:
        moderation_response = moderation_client.moderations.create(
            model="omni-moderation-latest",
            input=document_text[:4000]
        )

        flagged = moderation_response.results[0].flagged

        if flagged:
            return False, "Uploaded document failed OpenAI safety moderation."

        return True, "OpenAI input moderation passed."

    except Exception as e:
        return False, f"Input Moderation Error: {str(e)}"


def business_output_moderation(llm_output):

    prompt = f"""
    You are an AI governance validator for financial compliance systems.

    Review this AI generated compliance assessment and determine if it is safe for autonomous approval.

    Flag UNSAFE if:
    - severity is High
    - compliance score below 70
    - legal certainty is overstated
    - compliance assurance is too confident

    AI Output:
    {llm_output}

    Return only:
    SAFE
    or
    UNSAFE
    """

    response = moderation_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    verdict = response.choices[0].message.content.strip()

    if "SAFE" == verdict:
        return True, "Business governance moderation passed."
    else:
        return False, "Business governance moderation routed to human review."