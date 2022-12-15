from pynput.keyboard import Key, Controller
import time, kb, console

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
