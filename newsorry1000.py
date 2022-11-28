import pyautogui
import time
time.sleep(4)
count=4
while count<=1000:
    pyautogui.typewrite("sorry"+str(count))
    pyautogui.press("enter")
    count=count+1