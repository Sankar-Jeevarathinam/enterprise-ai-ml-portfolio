# 🏛️ FinPolicyLens Enterprise — Governed LLM Financial Policy Reviewer

FinPolicyLens Enterprise is a production-style Generative AI governance application designed to review financial service contracts, lending agreements, policy disclosures, and borrower-facing documentation using OpenAI LLMs under an enterprise-controlled approval framework.

The platform simulates how governed LLM systems can be deployed in regulated financial environments to identify ambiguous clauses, hidden fee exposure, disclosure weaknesses, customer-unfriendly language, and legal/compliance risks before policy approval.

---

## 🚀 Business Problem

Financial institutions process thousands of customer-facing contracts, loan agreements, disclosures, and servicing documents where vague or one-sided verbiage can create:

- borrower dissatisfaction
- regulatory compliance exposure
- disclosure transparency violations
- hidden fee disputes
- legal liability imbalance
- reputational risk

Traditional manual legal review is expensive, slow, and inconsistent.

FinPolicyLens Enterprise demonstrates how Large Language Models can accelerate first-pass compliance screening while still operating under human-governed approval safeguards.

---

## 🎯 Solution Overview

This application uses a governed multi-stage LLM review pipeline:

1. **Document Upload & PDF Parsing**
2. **OpenAI Input Moderation Check**
3. **LLM Document Type Classification**
4. **Financial Clause Extraction**
5. **Clause-by-Clause Risk Analysis via GPT**
6. **OpenAI Output Moderation Validation**
7. **Enterprise Model Approval Engine**
8. **Executive Governance Summary Generation**
9. **Downloadable AI Governance Review Report**

The final output provides both:
- clause-level compliance findings
- executive legal/compliance governance summary

---

## 🧠 Enterprise LLM Governance Architecture

```text
Financial PDF Upload
       ↓
OpenAI Input Moderation
       ↓
LLM Document Classification
       ↓
Reviewable Clause Detection
       ↓
GPT Financial Risk Clause Analysis
       ↓
OpenAI Output Moderation
       ↓
Enterprise Approval Engine
       ↓
Executive Governance Summary
       ↓
Download Governance Report
```

---

## 🔍 Key Financial Risks Detected

FinPolicyLens is engineered to identify enterprise-relevant borrower policy risks including:

- Hidden Fee Exposure
- Ambiguous Wording
- Disclosure Weakness
- Customer-Unfriendly Language
- Legal Liability Imbalance
- Weak Disclosure Transparency
- Readability Concerns

Each clause is scored with:

- Risk Category
- Severity Level
- Issue Found
- Compliance Explanation
- Recommended Safer Verbiage
- Compliance Score
- Approval Status
- Moderation Notes

---

## 🛡️ Governed AI Approval Workflow

Unlike a simple chatbot review, FinPolicyLens uses enterprise governance checkpoints:

### ✅ Input Moderation
Uploaded policy text is validated using OpenAI moderation endpoint before analysis.

### ✅ Output Moderation
Generated LLM recommendations are revalidated to ensure safe professional output.

### ✅ Model Approval Engine
High-risk or low-confidence clauses are automatically blocked from direct approval and routed to:

**Needs Human Review**

This simulates enterprise human-in-the-loop compliance governance.

---

## 📊 Dashboard Capabilities

The Streamlit dashboard provides:

- Governance Review Metrics
- Clause Risk Summary Table
- Severity Distribution Visualization
- Executive Compliance Narrative
- Expandable Detailed Clause Analysis
- Downloadable AI Governance PDF Report

---

## ⚙️ Tech Stack

- Python
- OpenAI GPT-4o-mini
- OpenAI Moderation API
- Streamlit
- Pandas
- Matplotlib
- ReportLab
- PyPDF2

---

## 🧪 Sample Financial Documents Tested

- Lending Agreements
- Borrower Disclosure Policies
- Servicing Fee Contracts
- Payment Penalty Clauses
- Financial Terms & Conditions

---

## 💼 Enterprise Use Cases

This governed LLM architecture can be extended for:

- Banking disclosure review
- Loan servicing agreement audit
- Insurance policy language review
- Mortgage borrower communication governance
- Internal compliance document QA
- Legal verbiage modernization

---

## 📸 Application Screenshots

### Main Governed Review Dashboard
(Add screenshot here)

### Clause Level Financial Risk Analysis
(Add screenshot here)

### Executive Governance Summary
(Add screenshot here)

---

## ▶️ How to Run Locally

```bash
git clone <your-repository-url>
cd 01-finpolicylens-enterprise-llm-governance
pip install -r requirements.txt
streamlit run app.py
```

Create a `.env` file:

```bash
OPENAI_API_KEY=your_openai_api_key
```

---

## 📁 Project Structure

```text
01-finpolicylens-enterprise-llm-governance/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_docs/
├── generated_reports/
├── screenshots/
└── src/
    ├── moderation.py
    ├── classifier.py
    ├── clause_extractor.py
    ├── llm_clause_reviewer.py
    ├── approval_engine.py
    ├── executive_summary.py
    ├── report_generator.py
    └── utils.py
```

---

## 🧾 Representative Output

- 5 reviewable clauses extracted from lending agreement
- 5 high-risk clauses flagged
- average compliance score generated
- automated safer borrower-friendly rewrite suggested
- all clauses routed through governed approval engine
- downloadable enterprise review report generated

---

## 🔮 Future Enhancements

- RAG-based regulatory citation validation
- OCR support for scanned legal documents
- Azure/OpenAI enterprise deployment
- reviewer feedback learning loop
- multi-document batch compliance scanning

---

## 👤 Author

Built as part of an Enterprise Applied GenAI / LLM Governance portfolio demonstrating practical use of OpenAI LLMs in regulated financial services compliance review.

