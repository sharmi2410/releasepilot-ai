# agents/risk_agent.py

def analyze_risk(commit_messages):
    risk_keywords = {
        "bug": "High",
        "fix": "Medium",
        "security": "Critical",
        "error": "High",
        "crash": "Critical",
        "update": "Low",
        "refactor": "Low",
        "feature": "Medium"
    }

    risk_report = []

    for commit in commit_messages:
        commit_lower = commit.lower()
        found = False

        for keyword, level in risk_keywords.items():
            if keyword in commit_lower:
                risk_report.append({
                    "commit": commit,
                    "risk_level": level
                })
                found = True
                break

        if not found:
            risk_report.append({
                "commit": commit,
                "risk_level": "Low"
            })

    return risk_report
