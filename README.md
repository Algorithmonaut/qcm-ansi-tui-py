This project is a simple TUI program that implement a MQC (QCM).

To obtain the data, the program uses a file called input.txt, located in the 
directory where it executes. 
In this file, the different entries are separated by a blank line, 
and each entry is composed of the question, followed by the index 
(starting at 1) of the good answer, followed by any number of possible answers.

##### For example:
```
What is my favorite color?
2
Red
Green 
Blue
```

Here the good answer to the question will be `Green`.

# Keymaps

- `Enter`: validate selected answer.
- `Escape`: exit program.
- `Up`/`Down` `arrows`: select up/down.
