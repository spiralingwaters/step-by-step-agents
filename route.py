#!/usr/bin/env python3

import os
import subprocess

# DEBUG OPTIONS
debug = True
showprompt = True
choice = input("Debug? (Y/n) ")
if choice.lower()=="n":
  debug = False
if debug:
  choice = input("Show full prompts? (Y/n) ")
  if choice.lower()=="n":
    showprompt = False

# RUN EXTERNAL SCRIPT
def run(arr):
  result = subprocess.run(arr, capture_output=True, text=True)
  return result.stdout

# WRITE TO FILE
def write(fname,contents):
  with open(f"{fname}",'w') as f:
    f.write(contents)

# READ TO FILE
def read(fname):
  with open(f"{fname}",'r') as f:
    return f.read()

# SET VARS

function = "route"
step = 0 #also see: 'step.txt'
output = ""

# RESET VARS IN FILE

write("step.txt","0")

# BEGIN LOOP

while True:

  # SET PATH FROM FUNCTION/STEP
  path = f"{function}/{step}"

  # SET 'STEP' FROM FILE
  step = read("step.txt").strip()
  try:
    step = int(step)
  except:
    step = 0
    if debug:
      print("DEBUG: step.txt is empty, set to '0'.")#DEBUG

  # RESET 'STEP' FILE
  write("step.txt","")
  # If 'step.txt' is set during the loop, then it's been set by a script and it won't be incremented normally at the end.



  # ROUTING by file ext:



  # GET USER INPUT
  if os.path.isfile(f"{path}.input"):
    if debug:
      print(f"{function}:{step}.input")
    output = input("\n"+"Say:")
    write("input.txt",output.strip())
    # No print, since its input
    if output=="quit" or output=="exit":
      break #break loop

  # RUN SCRIPT
  elif os.path.isfile(f"{path}.py"):
    if debug:
      print(f"{function}:{step}.py")
    output = run([f"{path}.py"]).strip()

  # LLM TEMPLATES, RUN LLM
  elif os.path.isfile(f"{path}.start") or os.path.isfile(f"{path}.start.py"):
    if debug:
      print(f"{function}:{step}:Prepare LLM template")
    # START PROMPT
    start_prompt=""
    if os.path.isfile(f"{path}.start"):
      start_prompt = read(f"{path}.start")
      if debug:
        print(f"{function}:{step}.start")
    elif os.path.isfile(f"{path}.start.py"):
      start_prompt = run([f"{path}.start.py"])
      if debug:
        print(f"{function}:{step}.start.py")
    # END PROMPT
    end_prompt=""
    if os.path.isfile(f"{path}.end"):
      end_prompt = read(f"{path}.end")
      if debug:
        print(f"{function}:{step}.end")
    elif os.path.isfile(f"{path}.end.py"):
      end_prompt = run([f"{path}.start.py"])
      if debug:
        print(f"{function}:{step}.end.py")

    # BUILD LLM PROMPT
    prompt = ""
    prompt += start_prompt
    if step==0:
      prompt += read("input.txt")
    else:
      prompt += output
    prompt += end_prompt
    if debug and showprompt:
      input(f"[PROMPT:{function}.{step}]"+prompt+f"[/PROMPT:{function}.{step}]")
    write("prompt.txt",prompt)

    # RUN LLM
    if debug:
      print("processing...")
    output = run(["oneshot","prompt.txt"])
    write("output.txt",output.strip())
    # LLM OUTPUT
    if len(output.strip())>0:
      print(f"\nAI: "+output.strip())

  # RESET FUNCTION/STEP
  else: #No more step files
    function = ""
    step = 0
    # OUTPUT: AFTER STEP FILES
    if len(output.strip())>0:
      print(f"\nAI: "+output.strip())
    if debug:
      print("write output.txt")

  # INCREMENT STEP
  step += 1

  # CAPTURE FUNCTION CALLS
  func = ""
  func = output.split("{{")
  if len(func)>1:
    func = func[1]
    func = func.split("}}")[0]

  # FUNCTION CALLS
  if len(func)>1:
    function = func
    # RESET STEP TO 0
    step = 0

  # DEFAULT FUNCTION
  if function=="":
    step = 0
    function = "route"

  # UPDATE STEP
  if read("step.txt").strip()!="":
    # STEP WAS UPDATED FROM SCRIPT
    newstep = read("step.txt")
    if int(newstep.strip())!=step+1:
      #update from file
      # only if step.txt is not predictable
      step = newstep
      if debug:
        print("Updated 'step.txt' from script.")#DEBUG
    else:
      #import time
      #time.sleep(1)
      write("step.txt",str(step))
  else:
    # STEP INCREMENTS NORMALLY
    #import time
    #time.sleep(1)
    write("step.txt",str(step))
  if debug:
    print(f"{function[:4]}.{step}...")

