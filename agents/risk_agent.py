# agents/risk_agent.py

def analyze_risk(commit_messages):

    risk_score = 0

    for commit in commit_messages:

        commit_lower = commit.lower()

        if (
            "auth" in commit_lower
            or "authentication" in commit_lower
            or "security" in commit_lower
        ):
            risk_score += 4

        elif (
            "payment" in commit_lower
            or "database" in commit_lower
        ):
            risk_score += 3

        elif (
            "fix" in commit_lower
            or "bug" in commit_lower
        ):
            risk_score += 2

        elif (
            "feat" in commit_lower
            or "feature" in commit_lower
        ):
            risk_score += 1

    if risk_score >= 8:
        risk_level = "High"

    elif risk_score >= 4:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level
    }