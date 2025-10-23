# Step-by-step Agents Framework

The 'Step-by-Step Agents Framework' is a file-driven LLM framework designed to be very easy to use, and the modular structure makes it simple to extend and customize. **No coding required**, _though Python scripting can be added at any step._

Each function is represented as a folder, and each step in that function is represented as numbered files in that folder.

## ✅ Features

- **File-driven Structure**: Everything is represented as folders and files, making it easy to manage.
- **Easy**: Create new functions/steps without coding.
- **Modular Design**: Functions can be easily added, removed, or disabled.
- **Extensible**: Use functions made by others just by adding their folder.
- **Crafted Prompts**: Define custom start/end prompts for each step.

## ✨ User Experience ✨

To get started, run "route.py" directly from the command line.

User input is first processed by the "{{route}}" function, which chooses which other function to route the user query to. Then the function it's routed to runs step by step, one prompt/script at a time, until it gets to the final answer for that user query.

### Flexibility

The routing of the original query allows the user to use casual language to engage any available functions.

### Predictability

The step-by-step crafted prompts allow developers to guide and constrict outputs to narrow outcomes so that the user always gets the appropriate response.

## 🧠 How It Works

First, the framework routes the user query to the appropriate "function" - with each function essentially consisting of a chain of custom LLM prompts. Then, the output of each step in the chain is then used as the input to the next step.

For instance, the first step could be a prompt that says "Write an outline about this topic:" and the next step can say "Write a short essay based on this outline:".

Any step file can also be a python script, which allows calling external programs, or loading dynamic content into the prompt itself.

## ✈️ Getting Started

### Installation

**WARNING:** 2.5GB LLM model will begin downloading as soon as you run "route.py"

* Requires ollama
* Requires 8GB RAM
* Requires 2.5GB harddrive space

Unzip **master-branch.zip** into any folder, and run "route.py" to get started!

### Which LLM?

By default the framework uses a script named "oneshot" to run the LLM prompt. This script simply takes a text file with a full LLM prompt as input, and prints out the LLM response. **This script can be _easily replaced_** by any script which acts the same.

#### Currently Uses: 

- Ollama
- Qwen3-abliterated:1.7B

**WARNING:** By default, this script uses ollama, and uses an abliterated(a.k.a. uncensored) version of Qwen3-1.7B of Q4_K_M quantization. This will require a 2.5GB download, and at least 6GB of RAM.

## 📂 Files:

- route.py
- step.txt
- output.txt
- input.txt
- route/
- math/
- chat/
- _**oneshot**_

The **route.py** script does all the work to keep track of which function you've selected, and progresses through the function step by step.

The **step.txt** file is used to keep track of which step you're on, and can be programmatically altered to change the flow of the function to skip steps or loop back to previous steps under certain conditions.

The **output.txt** file always saves the latest output.

The **input.txt** file always saves the initial user query before the function starts, to make it easy to reference the original query later.

Any **folder** whose name _does not_ begin with an underscore is considered a function. **route/** is the default function which routes the query to any other function. **math/** is an example of a tool usage function. **chat/** is an example of a looping function.

## 🧩 Functions

To add a function, you can just create a new folder.

To **disable a function**, or add a folder that isn't a function, just be sure to start the folder name with an **underscore**. Any folder starting with an underscore will be overlooked by the framework.

### info.txt

Each function requires a "info.txt" file, which describes when to call the function in as few words as possible. This is usually just one line.

```
{{route}} is the default function when no other functions are relevant.
```

### example.txt

Optionally, each function can include an "example.txt" which will give one or more examples of when it's appropriate to call that function. Remember, this file needs to include the appropriate LLM templates like the "<|im_start|>" and "<|im_end|>" type of stuff.

The {{route}} function doesn't include an example of when to call it, because it's just called automatically at the beginning of every query. But let's look at the "example.txt" file for the {{math}} function-

```
<|im_start|>user
What is eight times nine<|im_end|>
<|im_start|>assistant
{{math}}<|im_end|>
```

Notice that it doesn't include the system prompt. What the {{route}} function does is list all of the "info.txt" files for each function as a part of it's system prompt, to tell the LLM which functions are available. Then it includes all of the "example.txt" files one after another as if they were the first messages exchanged in the conversation.

## 👣 Step Files

Every step file starts with a number of which step it is, followed by a special file extension that signals to the framework what to do with that file.

### Basics

**.input** is used to signal the framework to ask for user input before proceeding. This can be used at any step.

**.start** and **.end** prompt templates indicate the start template and end template of a full LLM prompt. In this case, the .start and .end file start with the same number, since they're the same step, and the user input (or the output of the last step) is sandwiched between the .start and .end prompt. The LLM response of the whole thing all together is then passed as the output, either as the final output on the last step of the function, or as the output that is sent as input to the next step.

Remember, each prompt should stick to the appropriate LLM template:

#### Example

```
<|im_start|>system
<|im_end|>
<|im_start|>user
<|im_end|>
<|im_start|>assistant
```

### Advanced

Any step can include python scripting. This means you can use python to process results, load dynamic content into prompts, or call external programs.

There are two ways to use python scripts.

If the start or end template ends with ".py" such as **.start.py** or **.end.py**, then instead of using the text in the file as a start or end template, the framework uses the output of the script as the start or end template. This means you can dynamically load content into the prompt.

**.py**
If you put a script in that isn't named as a start or end template, it will simply call that script and use the output as the input to the next step. 

That means you can use programming to generate an answer without using the slow LLM response time. The more strategic text processing you can handle with programming, the less the LLM has to handle, and the shorter your response times.

This is also where you can implement "tool usage" by calling external programs.

## 🛠 Tool Usage

The {{math}} function is a good example of tool usage. Instead of asking the LLM to answer the math problem, the LLM is asked to create a python script to solve the math problem.

