from agents.severity_agent import analyze_severity
from agents.risk_agent import analyze_risk
from agents.stakeholder_agent import identify_stakeholders

def main():
    print("ReleasePilot AI Started")

    release_notes = "Fixed login bug and improved dashboard speed"

    severity = analyze_severity(release_notes)
    risk = analyze_risk(release_notes)
    stakeholders = identify_stakeholders(release_notes)

    print("Severity:", severity)
    print("Risk:", risk)
    print("Stakeholders:", stakeholders)

if __name__ == "__main__":
    main()
