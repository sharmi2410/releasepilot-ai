# agents/severity_agent.py
# agents/severity_agent.py

def analyze_severity(commit_messages):

    severity_keywords = {
        # Critical
        "critical": "Critical",
        "security": "Critical",
        "crash": "Critical",
        "auth": "Critical",
        "authentication": "Critical",
        "payment": "Critical",
        "database": "Critical",

        # High
        "bug": "High",
        "fix": "High",
        "error": "High",

        # Medium
        "feat": "Medium",
        "feature": "Medium",
        "update": "Medium",
        "add": "Medium",

        # Low
        "improve": "Low",
        "refactor": "Low",
        "clean": "Low",
        "docs": "Low"
    }

    severity_report = []

    for commit in commit_messages:

        commit_lower = commit.lower()
        severity_level = "Low"

        for keyword, level in severity_keywords.items():

            if keyword in commit_lower:
                severity_level = level
                break

        severity_report.append({
            "commit": commit,
            "severity": severity_level
        })

    return severity_report
