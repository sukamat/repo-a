"""
git-repo-sync is specifically written for Milo Floodgate repo setup process.
 - syncs code between two Git repositories
 - updates fstab.yaml file to point to floodgate content root in Sharepoint

Pre-requisite:
The script assumes that you have already setup a Floodgate repo as the "secondary" repo to sync to.
If not, follow the steps in the wiki before running this script: https://wiki.corp.adobe.com/display/WP4/Milo+Floodgate+Setup+For+Consumers

To run the script:
> python3 git-repo-sync.py
"""
import subprocess

# file to modify the sharepoint mount root
FSTAB_YAML_FILE = 'fstab.yaml'
# suffix to append to the mount root path
CONTENT_ROOT_SUFFIX = '-pink'

# git command to set repo-b as a mirror of repo-a
# git_command = ['git', 'remote', 'add', '--mirror=fetch', 'repob', 'git@github.com:sukamat/repo-b.git']

# # Output file path
# output_file_path = 'output.txt'

# # Execute the command and write the result to a text file
# with open(output_file_path, 'w') as output_file:
#     try:
#         subprocess.check_call(git_command, stdout=output_file, stderr=subprocess.STDOUT)
#         output_file.write('\nCommand executed successfully!')
#     except subprocess.CalledProcessError as e:
#         output_file.write(f'\nError: {e}')

# print(f'Result has been written to {output_file_path}')



# reset to origin
# subprocess.check_call(['git', 'reset', '--hard', 'origin'])
subprocess.check_call(['git', 'checkout', 'main'])
subprocess.check_call(['git', 'remote', 'add', '--mirror=fetch', 'repob', 'git@github.com:sukamat/repo-b.git'])

# read fstab.yaml and append '-pink' to the content root / mountpoint value
print('\n::: Updating fstab.yaml for pink repo :::\n')  
with open(FSTAB_YAML_FILE, "rb+") as file:
  file.seek(-1, 2)
  file.write((CONTENT_ROOT_SUFFIX + '\n').encode())   

# add, commit, and push to pink repo         
subprocess.check_call(['git', 'add', 'fstab.yaml'])
subprocess.check_call(['git', 'commit', '-m', 'Updated fstab.yaml with floodgate mountpoint'])
subprocess.check_call(['git', 'push', 'repob', '--all', '--force'])
print('\n::: fstab.yaml updated in pink repo and pushed to origin :::\n')

# reset to origin
subprocess.check_call(['git', 'reset', '--hard', 'origin'])
