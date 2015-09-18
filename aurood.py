#!/usr/bin/python
# find out-of-date AUR packages
# by: Florian Bruhin (The Compiler) <aurood@the-compiler.org>
# I hereby place this code in the public domain.

import json
import subprocess
import requests

out = subprocess.check_output(['pacman', '-Qm'], universal_newlines=True)
pkgs = [pkg.split()[0] for pkg in out.split('\n') if pkg]

payload = {'type': 'multiinfo', 'arg[]': pkgs}
json = requests.get('https://aur.archlinux.org/rpc.php', params=payload).json()

for result in json['results']:
    name = result['Name']
    if result['OutOfDate']:
        print(name)
