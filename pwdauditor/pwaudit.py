#!/bin/python
import os, tempfile, sys

print "This script assumes you are running some form of Kali linux"
print "kali is shipped with a copy of rockyou.txt, see comment for more info" #http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2


def goGetLists():        
        print "goGetLists started..."
        downloadTemp = tempfile.mkdtemp()
        os.system("cd" + downloadTemp)
#       os.system("wget https://crackstation.net/files/crackstation-human-only.txt.gz")
        os.system("ls")       



def getSpecificLists():
    return null

goGetLists()
