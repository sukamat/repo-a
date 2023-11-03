from github import Github
from github import InputGitTreeElement
from github.GithubException import GithubException
import uuid, datetime, re

# GitHub access token (generate one from https://github.com/settings/tokens)
access_token = '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'

# Repository names
source_repo_name = 'repo-a'
destination_repo_name = 'repo-b'
organization_name = 'sukamat'

# Initialize GitHub instance
g = Github(access_token)

# Create a new branch name
current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
unique_id = str(uuid.uuid4())
new_branch_name = f"sync_{current_date_time}_{unique_id}"
new_branch_name = re.sub(r'[^\w\s]', '-', new_branch_name)
print(f'New branch name: {new_branch_name}')

try:
    # Get source and destination repositories
    source_repo = g.get_repo(f'{organization_name}/{source_repo_name}')
    destination_repo = g.get_repo(f'{organization_name}/{destination_repo_name}')

    # Get source repository's default branch (usually 'main' or 'master')
    source_default_branch = source_repo.default_branch

    # Get the commit SHA of the source repository's default branch
    source_commit_sha = source_repo.get_commit(source_default_branch).sha

    # Get the tree of the latest commit in the source repository
    source_commit = source_repo.get_commit(source_commit_sha)
    source_tree_sha = source_commit.commit.tree.sha

    # Get commit message
    commit_message = source_commit.commit.message

    # Get the list of files in the source repository
    files = [file.filename for file in source_commit.files]

    destination_repo.create_git_ref(ref=f'refs/heads/{new_branch_name}', sha=source_commit_sha)

    # Get file contents and create files in destination repository
    for file_path in files:
        file_content = source_repo.get_contents(file_path, ref=source_default_branch)
        destination_repo.create_file(
            path=file_path,
            message=commit_message,
            content=file_content.content,
            branch=new_branch_name,  # Specify the destination branch
        )

    print(f'Code from {source_repo_name} has been pushed to {destination_repo_name}/fg-sync branch.')
except GithubException as e:
    print(f'Error : {e.data["message"]}')

