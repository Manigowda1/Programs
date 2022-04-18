import pywhatkit as py
import time
import pyautogui
import keyboard as k
r=15
for i in range(1,5):
    py.sendwhatmsg('+91***', 'Hi! This message is from Python', 8, r)
    pyautogui.click(1050, 950)
    time.sleep(2)
    k.press_and_release('enter')
    r=r+1


