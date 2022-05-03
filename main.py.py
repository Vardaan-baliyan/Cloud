import time

import pyautogui
import pynput.keyboard as kb
import win32api
import win32con

keyboard = kb.Controller()


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print('Left Click')
    #
    pyautogui.press("pagedown")
    time.sleep(20)


def RightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    print('Right Click')
    pyautogui.press("pagedown")
    time.sleep(20)


for i in range(100):
    for j in range(100):
        # RightClick()
        leftClick()
        time.sleep(80)
