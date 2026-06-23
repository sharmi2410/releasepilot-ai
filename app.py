import streamlit as st
from utils.github_reader import get_commits

st.title("ReleasePilot AI")

repo_url = st.text_input("Enter GitHub Repository URL")

if st.button("Analyze Repository"):
    commits = get_commits(repo_url)

    st.subheader("Recent Commit Messages")
    for commit in commits:
        st.write(commit)
