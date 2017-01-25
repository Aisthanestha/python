#/usr/bin/python3
import os
'''
This contains a list of Domains that are used by XBOX,
The whole reason this is a thing is because of Pi-hole
check it out at PI-HOLE.NET
'''
#list o' Domains
domains=['attestation.xboxlive.com','cert.mgt.xboxlive.com','ctldl.windowsupdate.com','def-vef.xboxlive.com','device.auth.xboxlive.com','eds.xboxlive.com','help.ui.xboxlive.com','licensing.xboxlive.com','notify.xboxlive.com','title.auth.xboxlive.com','title.mgt.xboxlive.com','www.msftncsi.com','www.xboxlive.com','xbox.ipv6.microsoft.com','xboxexperiencesprod.experimentation.xboxlive.com','xflight.xboxlive.com','xkms.xbolive.com','xsts.auth.xboxlive.com']

#look at the length of the domains and see how many times we need to iterate through it
bux=len(domains)
#starting at 0, x = 0, we go through each time, x increments, changes where we are in the string list
#run command every iteration 
for x in range(0,bux):
                foo=string[x]
                os.system('pihole -w %s' %foo)
                
