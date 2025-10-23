# Chat Function

This function stays in an endless loop of conversation, using 'start.prompt' as the AI character's system prompt. It saves a log of each exchange, and only loads only the last 4 exchanges into memory upon each new user query.

## Quirks

There is no 'exit' for this function, yet. It's an endless loop that needs to be stopped with a forced break.

Edit 'route.py' and set 'debug=True' for more debugging information on functions and their steps.

## Step Summary
0.
- Deletes 'logs/*'
- Loads 'start.prompt'
- Passes input from 'input.txt'
1.
- Writes first log file.
- (this only runs once)
2.
- Takes user input
3.
- Loads x most recent logs
- Loads 'start.prompt'
- Passes input from step 2
4.
- Writes next log file.
- Set step to '1', which really means '2' since 'step.txt' is automatically incremented between steps.

## Steps:

### STEP 0

- Deletes 'logs/*'
- Loads 'start.prompt'
- Passes input from 'input.txt'

The names "0.start.py" and "0.end" represent a chat template that utilizes scripting.

Any time a 'step 0' uses an LLM template, it receives 'input' from 'input.txt', so it will be the same input that was given to the {{route}} function. That functionality is hard-coded into 'route.py'

### STEP 1

- Writes next log file.

"1.py" is a script that runs, and passes it's output as input to the next step.

### STEP 2

- Takes user input

"2.input" indicates a request for user input. That user input is passed as the input to the next 'step', if the next step is an LLM template step.

### STEP 3

- Loads x most recent logs
- Loads 'start.prompt'
- Passes input from step 2

The names "3.start.py" and "3.end" represent a chat template that utilizes scripting.

### STEP 4

- Writes next log file.
- Set step to '1'

"4.py" is a script that runs, and passes it's output as input to the next step.

