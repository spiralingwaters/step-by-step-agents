#!/usr/bin/env python3

# STANDARD CHAT RESPONSE

# VARS
function = "chat"

# IMPORTS
import os

# LOAD STATIC PROMPT
with open(f"{function}/start.prompt",'r') as f:
  print(f.read().strip())

# LOAD DYNAMIC DATA
# Load the x latest logs.
logs = os.listdir(f"{function}/logs")

# CUSTOM NUMBER OF LOGS
nlogs = 4

# SORT LOGS BY NUMBER
logs = sorted(logs, key=lambda x: int(x)+1)
logs = "".join(logs[-nlogs:])

# LOAD LATEST X LOGS
for log in logs:
  with open(f"{function}/logs/{log}",'r') as f:
    print(f.read().strip())
