import time


def clear_screen():
    print("\033c", end="")


def prompt_choice(question, options):
    # options should be a list of strings with the options numbered
    while "the answer is invalid":
        print(question)
        for i in range(len(options)):
            print(str(i + 1) + ". " + options[i])
        reply = input("Enter the number of your choice: ")
        if reply.isdigit():
            if 0 < int(reply) <= len(options):
                return options[int(reply) - 1]


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


def print_countdown(seconds):
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)
