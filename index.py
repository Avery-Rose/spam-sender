import util
from util import *


def prompt_user_send():
    message = input("What message would you like to send? ")
    count = int(input("How many times would you like to send it? "))
    delay = float(input("How many seconds between each message? "))
    counter_enabled = console.yes_or_no("Would you like to include a counter in the message?")
    if counter_enabled:
        message += " ({}/{})"
    util.send_messages(message, count, delay, counter_enabled)


def prompt_user_delete():
    count = int(input("How many messages would you like to delete? "))
    delay = float(input("How many seconds between each message? (minimum 0.5) "))
    if delay < 0.5:
        delay = 0.5
        print("Invalid delay. Delay set to 0.5 seconds.")
    util.delete_messages(count, delay)


def main():
    console.clear_screen()
    while True:
        choice = console.prompt_choice("What would you like to do?", ["send", "delete", "exit"])
        if choice == "send":  # send
            prompt_user_send()
        elif choice == "delete":  # delete
            prompt_user_delete()
        elif choice == "exit":  # exit
            print("Exiting...")
            exit()
        else:
            print("Invalid choice.")


main()
