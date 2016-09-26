# removes old scripts folder, clones new repo


import os


print "Start of script..."
os.system("cd")
os.system("mkdir repo")
os.system("mv ~/repo/python/github_recloner.py ~/")
os.system("rm -r -d ~/repo")
print "0. python"
print "1. bash"
print "2. httpscreenshot"
print "3. config"
print "4. dvwa_installer"
valid="0"
while valid=="0":
    choice =raw_input("what repo do you want")
    if choice == "0":
    os.system("git clone https://github.com/aisthanestha/python")
    valid="1"
    elif choice == "1":
    os.system("git clone https://github.com/aisthanestha/bash")
    valid="1"
    elif choice == "2":
    os.system("git clone https://github.com/aisthanestha/httpscreenshot")
    valid="1"
    elif choice == "3":
    os.system("git clone https://github.com/aisthanestha/config")
    valid="1"
    elif choice == "4":
    os.system("git clone https://github.com/aisthanestha/dvwa_installer")
    valid="1"
    else: print "Enter a valid choice. (0-5)"
valid_remove=="0"
while valid_remove="0":
        choice_1 = raw_input("Remove ~/github_recloner.py?[y/n]")
        if choice_1 == "y" or choice_1 == "yes":
                print "removing ~/github_recloner.py"
                os.system("rm ~/github_recloner.py")
        elif choice_1 == "n" or choice_1 == "no":
                print "~/github_recloner.py remains"
        else: print "Enter valid choice. ('yes','y', 'n', 'no')

print "End of script.."

