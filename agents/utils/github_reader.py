import requests

def get_commits(repo_url):
    try:
        # Convert GitHub repo URL into API URL
        repo_name = repo_url.replace("https://github.com/", "")
        api_url = f"https://api.github.com/repos/{repo_name}/commits"

        response = requests.get(api_url)

        if response.status_code == 200:
            commits = response.json()

            commit_messages = []
            for commit in commits[:5]:   # Get latest 5 commits
                message = commit["commit"]["message"]
                commit_messages.append(message)

            return commit_messages
        else:
            return ["Error fetching commits"]

    except Exception as e:
        return [str(e)]
