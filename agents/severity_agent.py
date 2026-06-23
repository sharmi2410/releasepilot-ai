def analyze_severity(notes):
    if "bug" in notes.lower():
        return "Medium"
    return "Low"
