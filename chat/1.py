#!/usr/bin/env python3

# WRITE NEXT LOG FILE

# VARS
function = "chat"

# IMPORTS
import os

# FILEPATH
path = f"{function}/logs/"

# PROMPT TEMPLATE
mid = """<|im_end|>
<|im_start|>assistant
"""
end = """<|im_end|>
<|im_start|>user
"""

# GET INPUT/OUTPUT
inn = ""
outs = ""
with open("input.txt",'r') as f:
  inn = f.read().strip()
with open("output.txt",'r') as f:
  out = f.read().strip()

# BUILD PROMPT
prompt = ""
prompt += inn.strip()
prompt += mid
prompt += out.strip()
prompt += end
#input("DEBUG HERE:"+prompt)

# LOAD CHAT LOGS
logs = os.listdir(f"{path}")
# SORT LOGS BY NUMBER
logs = sorted(logs, key=lambda x: int(x))

# GET NEXT NUMBER
lastfile = 0
if len(logs)>0:
  lastfile = int(logs[-1])
nextfile = str(lastfile+1)

# WRITE NEXT LOG FILE
with open(f"{function}/logs/"+str(nextfile),'w') as f:
  f.write(prompt)

