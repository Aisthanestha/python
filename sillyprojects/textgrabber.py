#Navigate to folder to grab filenames to put into .txt

import os, string, sys


print "Current working directory, %s" % os.getcwd()

path = raw_input('Desired Path:')

print "The directory Chosen is\n", (path) 

os.chdir( path )


print "Current Directory: %s\n" % os.getcwd()

print "List of Current Directory %s\n\n\n\n" % os.listdir(".")

print "If its a file print it: %s\n\n" % os.path.isfile(".")





a = open("song.dat","a+")
for path, subdirs, files in os.walk(path):
        for filenames in subdirs:
                f = os.path(filenames)
                a.writelines(str(f)+ os.linesep)














#titles = os.listdir(".")
#dat = open('song.dat','a+')
#dat.writelines(titles)
#dat.close()


