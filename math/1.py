#!/usr/bin/env python3

output = ""

with open("output.txt",'r') as f:
  output = f.read()

def strip_codeblock(text):
    # Find the start and end of the code block
    start = text.find("```python") + len("```python")
    end = text.rfind("```")

    # Extract the code block
    if start < end:
        code = text[start:end].strip()
        return code
    else:
        return ""


output = strip_codeblock(output)
print(output)

with open("output.txt",'w') as f:
  f.write(output)

with open("math/math.py",'w') as f:
  f.write(output)
