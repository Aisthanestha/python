# removes old scripts folder, clones new repo


import os


print "Start of script..."
os.system("cd")
os.system("mv ~/scripts/github_recloner.py ~/")
os.system("rm -r -d ~/scripts")
os.system("git clone https://github.com/aisthanestha/scripts")
os.system("rm ~/github_recloner.py")
print "End of script.."

