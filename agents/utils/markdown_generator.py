def generate_markdown(commits, severity="Medium", risk="Low Risk", stakeholders=None):
    if stakeholders is None:
        stakeholders = []

    markdown_content = "# Release Notes\n\n"

    markdown_content += "## Commit Summary\n"
    for commit in commits:
        markdown_content += f"- {commit}\n"

    markdown_content += "\n## Severity Level\n"
    markdown_content += f"{severity}\n"

    markdown_content += "\n## Risk Analysis\n"
    markdown_content += f"{risk}\n"

    markdown_content += "\n## Stakeholders\n"
    for person in stakeholders:
        markdown_content += f"- {person}\n"

    return markdown_content
