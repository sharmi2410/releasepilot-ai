# agents/severity_agent.py

def analyze_severity(commit_messages):
    severity_keywords = {
        "critical": "Critical",
        "security": "Critical",
        "crash": "Critical",
        "bug": "High",
        "fix": "High",
        "error": "High",
        "feature": "Medium",
        "update": "Medium",
        "improve": "Low",
        "refactor": "Low",
        "clean": "Low"
    }

    severity_report = []

    for commit in commit_messages:
        commit_lower = commit.lower()
        severity_level = "Low"   # default

        for keyword, level in severity_keywords.items():
            if keyword in commit_lower:
                severity_level = level
                break

        severity_report.append({
            "commit": commit,
            "severity": severity_level
        })

    return severity_report
