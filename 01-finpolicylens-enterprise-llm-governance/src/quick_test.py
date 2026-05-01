from classifier import classify_document

txt = """
The borrower agrees to repay all lender imposed fees and penalties.
The lender may revise interest obligations without prior customer approval.
"""

print(classify_document(txt))