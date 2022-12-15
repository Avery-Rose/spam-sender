from pynput.keyboard import Key, Controller
import time

# ./kb.py
import kb
from kb import *
# ./console.py
import console
from console import *

keyboard = Controller()


def send_message(message):
    keyboard.type(message)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def send_messages(message, count, delay, counter_enabled):
    print("Sending " + str(count) + " messages with a delay of " + str(delay) + " seconds.")
    print("Sending in 5 seconds...")
    console.print_countdown(5)
    print("Sending messages...")
    start_time = time.time()
    for i in range(count):
        if counter_enabled:
            send_message(message.format(i + 1, count))
        else:
            send_message(message)
        print("Sent message " + str(i + 1) + " of " + str(count))
        time.sleep(delay)
    end_time = time.time()
    time_elapsed = round(end_time - start_time, 2)
    print("Finished in " + str(time_elapsed) + " seconds.")


def delete_message():
    kb.focus_chat()
    kb.press(Key.up)
    kb.select_all()
    # delete text
    kb.press(Key.backspace)
    kb.press(Key.enter)
    # confirm deletion popup
    time.sleep(0.2)
    kb.press(Key.enter)


def delete_messages(count, delay):
    print("Deleting " + str(count) + " messages with a delay of " + str(delay) + " seconds.")
    print("Deleting in 5 seconds...")
    console.print_countdown(5)
    print("Deleting messages...")
    start_time = time.time()
    for i in range(count):
        delete_message()
        print("Deleted message " + str(i + 1) + " of " + str(count))
        time.sleep(delay)
    end_time = time.time()
    # round to 2 decimal places the time elapsed
    time_elapsed = round(end_time - start_time, 2)
    print("Finished in " + str(time_elapsed) + " seconds.")


def prompt_user_send():
    message = input("What message would you like to send? ")
    count = int(input("How many times would you like to send it? "))
    delay = float(input("How many seconds between each message? "))
    counter_enabled = console.yes_or_no("Would you like to include a counter in the message?")
    if counter_enabled:
        message += " ({}/{})"
    send_messages(message, count, delay, counter_enabled)


def prompt_user_delete():
    count = int(input("How many messages would you like to delete? "))
    delay = float(input("How many seconds between each message? (minimum 0.5) "))
    if delay < 0.5:
        delay = 0.5
    delete_messages(count, delay)


def main():
    console.clear_screen()
    while True:
        choice = console.prompt_choice("Would you like to send or delete messages?", ["send", "delete", "exit"])
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
