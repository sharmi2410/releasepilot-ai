from utils.github_reader import get_commits

repo_url = input("Enter GitHub Repo URL: ")

print("\nAnalyzing Repository...\n")

commits = get_commits(repo_url)

for commit in commits:
    print(commit)
