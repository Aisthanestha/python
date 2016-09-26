import os 

a = open("song.dat","a+")
for path, subdirs, files in os.walk(r" ~/Documents/Music"):
        for filename in files:
                f = os.path.join(path, filename)
                a.write(str(f)+os.linsep)
