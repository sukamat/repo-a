import subprocess
# import os

# # Repository names
# source_repo_name = 'repo-a'
# destination_repo_name = 'repo-b'
# organization_name = 'sukamat'

# # Read GitHub access token from GitHub Secrets
# access_token = os.environ.get('GH_TOKEN_ALL')
# if access_token is None:
#     raise ValueError('GitHub access token is not set')


# git config --global user.email "santoshkumar.sn@gmail.com"
#           git config --global user.name "skumar09"
# git config --global url.https://${{ secrets.GITHUB_TOKEN }}@github.com/.insteadOf https://github.com/          
#           git remote set-url repob https://$GITHUB_TOKEN@github.com/sukamat/repo-b.git

# subprocess.check_call(['git', 'config', 'user.email', 'sukamat@adobe.com'])
# subprocess.check_call(['git', 'config', 'user.name', 'sukamat'])
# subprocess.check_call(['git', 'config', 'url.https://${{ secrets.GITHUB_TOKEN }}@github.com/.insteadOf', 'https://github.com/'])
# subprocess.check_call(['git', 'remote', 'set-url', 'repob', 'https://$GITHUB_TOKEN@github.com/sukamat/repo-b.git'])
# subprocess.check_call(['git', 'remote', 'add', '--mirror=fetch', 'repob', 'git@github.com:sukamat/repo-b.git'])

# git ls-remote https://$GH_PAT1@github.com/skumar09/testreport.git
# subprocess.check_call(['git', 'ls-remote', 'https://$GITHUB_TOKEN@github.com/sukamat/repo-b.git'])

# subprocess.check_call(['git', 'checkout', 'main'])
# subprocess.check_call(['git', 'clone', 'https://github.com/sukamat/repo-b.git', 'repo-b'])

# subprocess.check_call(['cp', '-fr', '.', 'repo-b'])