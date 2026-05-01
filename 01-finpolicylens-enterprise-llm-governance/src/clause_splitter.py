import re

def split_into_clauses(document_text):

    raw_chunks = re.split(r'\n+|(?<=\.)\s+', document_text)

    clauses = []

    for chunk in raw_chunks:
        cleaned = chunk.strip()

        if len(cleaned) > 80:
            clauses.append(cleaned)

    return clauses[:5]