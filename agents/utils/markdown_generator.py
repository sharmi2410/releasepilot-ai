# agents/utils/markdown_generator.py

def generate_markdown(severity_report):

    markdown = "# ReleasePilot AI Report\n\n"

    markdown += "## Commit Analysis\n\n"

    for item in severity_report:

        markdown += f"### Severity: {item['severity']}\n"
        markdown += f"- {item['commit']}\n\n"

    return markdown


# Test Code
if __name__ == "__main__":

    sample_data = [
        {
            "commit": "Fix authentication bug",
            "severity": "Critical"
        },
        {
            "commit": "Update app.py",
            "severity": "Medium"
        },
        {
            "commit": "Refactor UI code",
            "severity": "Low"
        }
    ]

    report = generate_markdown(sample_data)

    print(report)