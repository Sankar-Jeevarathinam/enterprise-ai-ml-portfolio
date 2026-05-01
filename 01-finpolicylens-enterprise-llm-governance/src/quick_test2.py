# -*- coding: utf-8 -*-

from llm_reviewer import review_clause_with_llm

clause = "The lender may impose additional servicing charges and modify repayment obligations without prior borrower consent."

result = review_clause_with_llm(clause, "Lending Agreement")

print(result)
