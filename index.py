from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def send_message(message):
    keyboard.type(message)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def prompt_user():
    message = input("What message would you like to send? ")
    count = int(input("How many times would you like to send it? "))
    delay = float(input("How many seconds between each message? "))
    counter_enabled = input("Would you like to include a counter? (y/n) ")
    if counter_enabled == "y":
        message += " ({}/{})"
    return message, count, delay


def main():
    message, count, delay = prompt_user()
    print("Sending " + str(count) + " messages with a delay of " + str(delay) + " seconds.")
    print("Sending in 5 seconds...")
    print_countdown(5)
    for i in range(count):
        if "{}/{}" in message:
            send_message(message.format(i + 1, count))
        else:
            send_message(message)
        time.sleep(delay)
    print("Done!")


def print_countdown(seconds):
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)
    print("Sending messages...")


main()
