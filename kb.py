from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def press(key):
    keyboard.press(key)
    keyboard.release(key)


def hold(key):
    keyboard.press(key)


def release(key):
    keyboard.release(key)


def focus_chat():
    hold(Key.alt)
    press("c")
    release(Key.alt)


def select_all():
    time.sleep(0.1)
    hold(Key.ctrl)
    press("a")
    release(Key.ctrl)
    time.sleep(0.1)
