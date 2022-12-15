from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def press(key):
    keyboard.press(key)
    keyboard.release(key)


def type(message):
    keyboard.type(message)


def hold(key):
    keyboard.press(key)


def release(key):
    keyboard.release(key)


def focus_chat():
    hold(Key.alt)
    press("c")
    release(Key.alt)
    time.sleep(0.1)


def select_all():
    time.sleep(0.1)
    hold(Key.ctrl)
    press("a")
    release(Key.ctrl)
    time.sleep(0.1)
