import re
import subprocess


def get_git_repo_details():
    git_remote_url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"], text=True).strip()
    url_pattern = re.compile(r"(?:git@github\.com:|https://github\.com/)([\w.-]+)/([\w.-]+)(?:\.git)?$")
    match = url_pattern.match(git_remote_url)

    if match is None:
        raise ValueError("Unable to parse git repository URL")

    git_owner, repo_name = match.group(1), match.group(2)
    return git_owner, repo_name
