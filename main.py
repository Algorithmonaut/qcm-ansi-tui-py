import sys
import termios
import tty
import random

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
    
    entries = content.split('\n\n')  # Split entries by blank lines
    parsed_data = []

    for entry in entries:
        lines = entry.strip().split('\n')
        question = lines[0]
        correct_answer_index = int(lines[1]) - 1  # Convert to 0-based index
        answers = lines[2:]
        
        if not 0 <= correct_answer_index < len(answers):
            print("[ERROR] Invalid correct answer index")
            exit(1)
        
        parsed_data.append({
            'question': question,
            'correct_answer_index': correct_answer_index + 1,  # Convert back to 1-based index
            'answers': answers
        })
    
    return parsed_data

################################################################################

current_row = 0

# ANSI escape sequences 
RESET = "\033[0m" # Resets text formatting to default
INVERT = "\033[7m" # Invert foreground and background color

CURSOR_HIDE = "\033[?25l"  # ANSI sequence to hide cursor
CURSOR_SHOW = "\033[?25h"  # ANSI sequence to show cursor

def clear_console():
    print("\033[H\033[J", end="")

def print_question(selected_row_idx, question, answers):
    clear_console()

    print("\033[1m" +  question + RESET)

    for idx, row in enumerate(answers):
        if idx == selected_row_idx:
            print(f"{INVERT}{row}{RESET}")
        else:
            print(row)

def quit():
    print(CURSOR_SHOW)
    clear_console()
    print("Exiting program...")
    sys.exit()

def getch():
    # Read a single character from the standard input 
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def validate_answer(correct_answer, answer):
    right_messages = [
        "Absolutely right!",
        "Spot on! You're correct!",
        "You're a genius! Right answer!",
        "You've got it! Well done!",
        "Correctomundo!",
        "Nailed it! You're right!",
        "Right as rain!",
        "You're on fire! That's correct!",
        "You're crushing it! Right answer!",
        "Brilliant! You're correct!"
    ]

    wrong_messages = [
        "Oops, that's not it!",
        "Close, but no cigar!",
        "Not quite there, try again!",
        "That's incorrect, sorry!",
        "Incorrecto!",
        "Better luck next time!",
        "Nope, not this time!",
        "That's a swing and a miss!",
        "Sorry, that's not the right one!",
        "Not the answer we were looking for!"
    ]

    print()

    if correct_answer == answer:
        print("\033[92m" + random.choice(right_messages) + RESET)

    else:
        print("\033[91m" + random.choice(wrong_messages) + RESET)
        print("The correct answer was:\n\"" + correct_answer + "\"")

    print("Press enter to continue...")

    key = getch()
    while key not in ('\n', '\r'):
        if key == 'q':
            quit()
        key = getch()

def main():
    print(CURSOR_HIDE)

    global current_row

    file_path = 'input.txt'
    parsed_data = parse_input_file(file_path)
    for entry in parsed_data:
        answers = entry["answers"]

        print_question(current_row, entry["question"], answers)

        while True:
            key = getch()
            if key == '\x1b':   # Arrow keys are preceded by an ESC sequence in most terminal env
                next1, next2 = getch(), getch()
                if next1 == '[':
                    if next2 == 'A':  # Up arrow
                        current_row = (current_row - 1) % len(answers)
                    elif next2 == 'B':  # Down arrow
                        current_row = (current_row + 1) % len(answers)

            elif key in ('\n', '\r'):  # Enter key
                validate_answer(answers[entry["correct_answer_index"] - 1],
                                answers[current_row])
                break

            elif key == 'q':
                quit()


            print(entry["question"])
            print_question(current_row, entry["question"], answers)

    print(CURSOR_SHOW)


main()
