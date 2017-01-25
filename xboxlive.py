#/usr/bin/python3
import os
'''
So now that i got this pi, i have redone it on a couple networks and i keep having to add these domains for my xbox to actually work, so why do it more than once, lets just make a le scripto
'''
string=['attestation.xboxlive.com','cert.mgt.xboxlive.com','ctldl.windowsupdate.com','def-vef.xboxlive.com','device.auth.xboxlive.com','eds.xboxlive.com','help.ui.xboxlive.com','licensing.xboxlive.com','notify.xboxlive.com','title.auth.xboxlive.com','title.mgt.xboxlive.com','www.msftncsi.com','www.xboxlive.com','xbox.ipv6.microsoft.com','xboxexperiencesprod.experimentation.xboxlive.com','xflight.xboxlive.com','xkms.xbolive.com','xsts.auth.xboxlive.com']
for x in range(0,18):
                numberIn=string[x]
                os.system('pihole -w %s' %numberIn)

