def analyze_risk(notes):
    if "fixed" in notes.lower():
        return "Low Risk"
    return "High Risk"
