from moderation import business_output_moderation

def approve_model_response(parsed_response, raw_output):

    try:
        score = int(parsed_response["Compliance Score"])
        severity = parsed_response["Severity"].lower()

        if severity == "high" or score < 70:
            parsed_response["Approval Status"] = "Needs Human Review"
            parsed_response["Moderation Note"] = "High risk clause blocked by approval engine"
            return parsed_response

        passed, note = business_output_moderation(raw_output)

        if passed:
            parsed_response["Approval Status"] = "Model Approved"
            parsed_response["Moderation Note"] = note
        else:
            parsed_response["Approval Status"] = "Needs Human Review"
            parsed_response["Moderation Note"] = note

    except:
        parsed_response["Approval Status"] = "Needs Human Review"
        parsed_response["Moderation Note"] = "Approval engine exception"

    return parsed_response