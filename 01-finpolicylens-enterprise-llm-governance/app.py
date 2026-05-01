import streamlit as st
import matplotlib.pyplot as plt
from parser import extract_text_from_pdf
from classifier import classify_document
from moderation import input_moderation
from clause_splitter import split_into_clauses
from llm_reviewer import review_clause_with_llm
from response_parser import parse_llm_response
from approval_engine import approve_model_response
from report_generator import generate_summary_report
from executive_summary import generate_executive_summary

st.set_page_config(page_title="FinPolicy Lens Enterprise", layout="wide")

st.title("🏦 FinPolicy Lens Enterprise — Governed LLM Financial Policy Reviewer")

uploaded_file = st.file_uploader("Upload Financial Policy / Contract PDF", type=["pdf"])

if uploaded_file:

    with st.spinner("Extracting document text..."):
        full_text = extract_text_from_pdf(uploaded_file)

    valid, msg = input_moderation(full_text)

    if not valid:
        st.error(msg)

    else:
        st.success(msg)

        with st.spinner("Running LLM document classification..."):
            doc_type = classify_document(full_text)

        st.info(f"Document Classified As: {doc_type}")

        clauses = split_into_clauses(full_text)
        st.write(f"Detected {len(clauses)} reviewable clauses for governed AI review.")

        if st.button("Run Governed AI Review"):

            approved_results = []

            progress_bar = st.progress(0)

            for i, clause in enumerate(clauses):

                raw_llm = review_clause_with_llm(clause, doc_type)
                parsed = parse_llm_response(raw_llm)
                approved = approve_model_response(parsed, raw_llm)
                approved["Clause"] = clause[:120]

                approved_results.append(approved)
                progress_bar.progress((i + 1) / len(clauses))

            df, summary = generate_summary_report(approved_results)
            summary_text = generate_executive_summary(df, doc_type)

            st.markdown("---")
            st.subheader("📊 Governance Review Metrics")
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Clauses Reviewed", len(df))
            m2.metric("Flagged Clauses", len(df[df["Compliance Score"] < 80]))
            m3.metric("Average Compliance Score", round(df["Compliance Score"].mean(), 1))
            
            
            left, right = st.columns([2,1])
            
            with left:
                st.subheader("📋 Clause Risk Summary")
                summary_df = df[[
                    "Risk Category",
                    "Severity",
                    "Compliance Score",
                    "Approval Status"
                ]]
                st.dataframe(summary_df, use_container_width=True)
            
            with right:
                st.subheader("📈 Severity Distribution")
                severity_counts = df["Severity"].value_counts()
            
                fig, ax = plt.subplots(figsize=(3.2,2.2))
                ax.bar(severity_counts.index, severity_counts.values)
                ax.tick_params(axis='x', labelsize=8)
                ax.tick_params(axis='y', labelsize=8)
                plt.tight_layout()
                st.pyplot(fig)
            
            
            needs_review = len(df[df["Approval Status"] == "Needs Human Review"])
            
            if needs_review > 0:
                st.warning(f"{needs_review} clauses routed for mandatory human review.")
            else:
                st.success("All clauses passed model approval governance.")
            
            
            st.subheader("🧠 LLM Executive Governance Summary")
            st.write(summary_text)
            
            with st.expander("View Detailed Clause Analysis"):
                st.dataframe(df, use_container_width=True)
            
            st.download_button(
                "📥 Download AI Governance Review Report",
                df.to_csv(index=False),
                "governance_review_report.csv"
            )