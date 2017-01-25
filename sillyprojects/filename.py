import os 

path=input("Enter Desired Path: ")#Take user input for a path to somewhere on the filesystem
os.chdir(path)#Change to user specified DIR
os.system('pwd')#Let's see where we are actually at

os.system('ls | cat >> dir.txt')#list directory currently within, pipe ls into cat and feed cat into dir.txt > would overwrite previous dir.txt as >> appends

