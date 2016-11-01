import os
# this will create a rainbow table that is loweralpha-numerica abcd...1234... with a plaintext length min of 6 and max of 6 with table index from 0 to 10 so it will take a while to generate. 
print "start of script..."
os.system("cd /usr/share/rainbowcrack")
for i in range (0, 11):
        os.system("rtgen md5 loweralpha-numeric 6 6 %s 3500 100000 0" % i)#makes 11 tables total 0-11
os.system("rtsort *.rt") #sorts all .rt files in /usr/share/rainbowcrack
print "end of script..."
