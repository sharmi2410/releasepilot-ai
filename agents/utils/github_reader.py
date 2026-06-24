import subprocess

def get_commits():

    try:
        result = subprocess.check_output(
            ["git", "log", "--pretty=%s", "-n", "5"],
            text=True
        )

        commits = result.strip().split("\n")

        return commits

    except Exception as e:
        return [str(e)]


print(get_commits())