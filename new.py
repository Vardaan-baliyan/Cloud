import time
import win32api, win32con
import win32evtlogutil
import win32evtlog
import pynput.keyboard as kb
import pyautogui
from pynput.keyboard import Key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

keyboard=kb.Controller()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('Left Click')
    time.sleep(55)
    pyautogui.press("pagedown")
    time.sleep(50)

def RightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    print('Right Click')
    time.sleep(50)

for i in range (100):
    for j in range (100):
     RightClick()
     leftClick()