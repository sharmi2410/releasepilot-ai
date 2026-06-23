# agents/stakeholder_agent.py

def identify_stakeholders(commit_messages):
    stakeholder_rules = {
        "security": ["Security Team", "Admin"],
        "bug": ["Developers", "QA Team"],
        "fix": ["Developers", "QA Team"],
        "feature": ["Product Manager", "Developers"],
        "ui": ["UI/UX Team", "Product Manager"],
        "database": ["Database Admin", "Developers"],
        "payment": ["Finance Team", "Product Manager"]
    }

    stakeholder_report = []

    for commit in commit_messages:
        commit_lower = commit.lower()
        assigned = ["Developers"]   # default

        for keyword, team in stakeholder_rules.items():
            if keyword in commit_lower:
                assigned = team
                break

        stakeholder_report.append({
            "commit": commit,
            "stakeholders": assigned
        })

    return stakeholder_report
