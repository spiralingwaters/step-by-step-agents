#!/usr/bin/env python3

import subprocess

output = ""

with open("output.txt",'r') as f:
  output = f.read()
result = subprocess.run(["python3","math/math.py"], capture_output=True, text=True)
output = result.stdout

with open("output.txt",'w') as f:
  f.write(output)

# OUTPUT
print(output.strip())
