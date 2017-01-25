#!/usr/bin/python3
#average user just get it from their site
import os
os.system('curl -sSL https://install.pi-hole.net | cat > install_pihole.sh | bash')
print('hopefully setup complete')
os.system('python3 xboxlive.py')

