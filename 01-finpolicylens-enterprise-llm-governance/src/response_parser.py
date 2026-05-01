import json

def parse_llm_response(llm_output):

    try:
        parsed = json.loads(llm_output)
        
        parsed["Severity"] = str(parsed.get("Severity", "Medium")).title()
        parsed["Risk Category"] = str(parsed.get("Risk Category", "Unknown")).title()
        
        parsed["Compliance Score"] = int(parsed.get("Compliance Score", 50))

        required_fields = [
            "Risk Category",
            "Severity",
            "Issue Found",
            "Explanation",
            "Recommended Safer Verbiage",
            "Compliance Score"
        ]

        for field in required_fields:
            if field not in parsed:
                parsed[field] = ""

        parsed["Compliance Score"] = int(parsed.get("Compliance Score", 50))

        return parsed

    except:
        return {
            "Risk Category": "Parsing Failure",
            "Severity": "High",
            "Issue Found": "LLM JSON parsing failed",
            "Explanation": "Model returned malformed response",
            "Recommended Safer Verbiage": "Human review required",
            "Compliance Score": 10
        }