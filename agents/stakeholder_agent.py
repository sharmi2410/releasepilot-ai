# agents/stakeholder_agent.py

def generate_stakeholder_summary(commit_messages):

    summaries = []

    for commit in commit_messages:

        commit_lower = commit.lower()

        if "auth" in commit_lower or "security" in commit_lower:
            summary = {
                "stakeholder": "Manager",
                "message": "Security-related changes were made. Extra testing and review are recommended."
            }

        elif "fix" in commit_lower or "bug" in commit_lower:
            summary = {
                "stakeholder": "QA Team",
                "message": "A bug fix was introduced. Please verify functionality before release."
            }

        elif "feature" in commit_lower or "feat" in commit_lower or "add" in commit_lower:
            summary = {
                "stakeholder": "Product Team",
                "message": "A new feature was added. Update product documentation if required."
            }

        else:
            summary = {
                "stakeholder": "Developer",
                "message": "Minor code updates detected with low business impact."
            }

        summaries.append({
            "commit": commit,
            "stakeholder": summary["stakeholder"],
            "message": summary["message"]
        })

    return summaries


# Test Code
if __name__ == "__main__":

    sample_commits = [
        "Fix authentication bug",
        "Add payment feature",
        "Update app.py"
    ]

    result = generate_stakeholder_summary(sample_commits)

    for item in result:
        print(item)