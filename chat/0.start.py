#!/usr/bin/env python3

# INITIAL CHAT RESPONSE

# VARS
function = "chat"

# IMPORTS
import os
import subprocess

# LOAD STATIC PROMPT
with open(f"{function}/start.prompt",'r') as f:
  print(f.read().strip())

# Remove all chat logs.
logs = os.listdir(f"{function}/logs")
for x in logs:
  subprocess.run(["rm","-rf",f"{function}/logs/{x}"])
